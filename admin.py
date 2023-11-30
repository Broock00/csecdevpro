from django.contrib import admin
from .models import CustomUser, Event, SpecialAnnouncement


admin.site.site_header = 'CSEC_ASTU'
admin.site.site_title = 'Admin site'
admin.site.index_title = 'Admin administration'


@admin.register(CustomUser)
class CustomUseradmin(admin.ModelAdmin):
    fields = ('username','User_ID','Phone_number','Department','password')
    list_filter = ('Department',)
    list_display = ('username','User_ID','Phone_number','Department')
    # ordering = ('Today',)
    search_fields = ('username',)


@admin.register(Event)
class Eventadmin(admin.ModelAdmin):
    list_filter = ('Event_name','Event_type')
    list_display = ('Event_name','Event_type','Location','Organizer')
    ordering = ('Today',)
    search_fields = ('Event_name',)
    

admin.site.register(SpecialAnnouncement)