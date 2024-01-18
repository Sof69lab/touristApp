from django.contrib import admin
from touristapp.models import Tour, Reservation
from django.contrib.admin.models import LogEntry

admin.site.register(Tour)
admin.site.register(Reservation)
admin.site.register(LogEntry)