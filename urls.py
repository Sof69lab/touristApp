from django.urls import path, re_path
from touristapp import views

urlpatterns = [
    re_path(r'^$', views.TourView.as_view(), name='tours'),
    re_path(r'^registration/$', views.registration, name='registration'),
    re_path(r'^tour/(?P<pk>\d+)$', views.TourDetail.as_view(), name='tour-detail'),
    re_path(r'^user/(?P<pk>\d+)$', views.profile.as_view(), name='profile_detail'),
    re_path(r'^user/edit', views.profileUpdate.as_view(), name='profile_edit'),
    re_path(r'^contacts/$', views.contacts, name='contacts'),
]
