from django.contrib import admin

from .models import Concurs,Participant


@admin.register(Concurs)
class ConcursAdmin(admin.ModelAdmin):
    list_display = ['header','data']

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['fest_id','surname','name','email']
    ordering = ['-id']