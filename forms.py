from django import forms
from django.contrib.auth.models import User
from touristapp.models import Reservation

class DetailForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('name', 'start_date', 'end_date', 'user', 'people', 'cost')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')
