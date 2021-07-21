from django.contrib import admin

from .models import Trip

class TripAdmin(admin.ModelAdmin):
    list_display = ('author', 'country', 'destination', 'start', 'end',)

admin.site.register(Trip, TripAdmin)