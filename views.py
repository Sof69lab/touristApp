from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from touristapp.models import Tour, Reservation
from touristapp.forms import DetailForm, UserForm
from django.db import transaction
from django.db.models import Q
import datetime

class TourView(ListView):
    model = Tour
    template_name = "tours.html"
    context_object_name = 'tours'
    def get_queryset(self):
        query = self.request.GET.get("q")
        queryMinDur = self.request.GET.get("qmind")
        queryMaxDur = self.request.GET.get("qmaxd")
        queryMinPr = self.request.GET.get("qminp")
        queryMaxPr = self.request.GET.get("qmaxp")
        if queryMinDur == '' or queryMinDur is None:
            queryMinDur = 0
        if queryMaxDur == '' or queryMaxDur is None:
            queryMaxDur = 10000000
        if queryMinPr == '' or queryMinPr is None:
            queryMinPr = 0
        if queryMaxPr == '' or queryMaxPr is None:
            queryMaxPr = 10000000
        if query is not None and query != '':
            object_list = Tour.objects.filter(
                (Q(name__icontains=query) | Q(route__icontains=query) | Q(transport__icontains=query) | Q(describe__icontains=query))
                & Q(duration__range=(float(queryMinDur)*24, float(queryMaxDur)*24+1)) & Q(price__range=(float(queryMinPr), float(queryMaxPr)+1))
            )
        else:
            if queryMinDur == 0 and queryMaxDur == 10000000 and queryMinPr == 0 and queryMaxPr == 10000000:
                object_list = Tour.objects.all()
            else:
                object_list = Tour.objects.filter(
                    Q(duration__range=(float(queryMinDur)*24, float(queryMaxDur)*24+1)) & Q(price__range=(float(queryMinPr), float(queryMaxPr)+1))
                )
        return object_list

class TourDetail(DetailView):
    model = Tour
    template_name = 'tour_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TourDetail, self).get_context_data(**kwargs)
        context['form'] = DetailForm
        return context

    def post(self, request, *args, **kwargs):
        form = DetailForm(data=request.POST)
        model2 = Reservation()
        current_date = datetime.datetime.now().date()
        if form.is_valid():
            if form.cleaned_data.get('start_date') > current_date:
                model2.user = form.cleaned_data.get('user')
                model2.name = form.cleaned_data.get('name')
                model2.start_date = form.cleaned_data.get('start_date')
                model2.end_date = form.cleaned_data.get('end_date')
                model2.people = form.cleaned_data.get('people')
                model2.cost = form.cleaned_data.get('cost')
                model2.save()
            else:
                form.add_error('start_date', 'Нельзя забронировать тур на текущую или прошедшую дату')
        self.object = self.get_object()
        context = super(TourDetail, self).get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context=context)

class profile(DetailView):
    model = User
    template_name = 'profile_detail.html'
    def get_object(self, queryset=None):
        return self.request.user
    def get_context_data(self, **kwargs):
        context = super(profile, self).get_context_data(**kwargs)
        context['form'] = DetailForm
        return context
    def get(self, request, *args, **kwargs):
        form = DetailForm(data=request.GET)
        current_date = datetime.datetime.now().date()
        model2 = Reservation.objects.filter(user=self.request.user)
        reservs = ""
        for i in model2:
            if i.start_date >= current_date:
                reservs += i.name.name + ' ' + str(i.start_date)
                if (str(i.start_date) != str(i.end_date)):
                    reservs += ' - ' + str(i.end_date)
                reservs += ' ' + str(i.people) + 'чел.'
                reservs += ' ' + str(i.cost) + 'руб.'
                reservs += "\n"
        self.object = self.get_object()
        context = super(profile, self).get_context_data(**kwargs)
        context['form'] = DetailForm
        context['reservs'] = reservs
        # return self.render_to_response(context=context)
        return render(request, self.template_name, context=context)
        # for i in model2:
        #     form.initial({'name': i.name.name})

class profileUpdate(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'profile_edit.html'
    def get_object(self, queryset=None):
        return self.request.user
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['form'] = UserForm(self.request.POST, instance=self.request.user)
        else:
            context['form'] = UserForm(instance=self.request.user)
        return context
    def form_valid(self, form_class):
        context = self.get_context_data()
        user_form = context['form']
        with transaction.atomic():
            if all([form_class.is_valid(), user_form.is_valid()]):
                user_form.save()
                form_class.save()
                return self.render_to_response(context)
            else:
                context.update({'form': user_form})
                return self.render_to_response(context)


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def contacts(request):
    return render(request, "contacts.html", {})
