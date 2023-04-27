from django.contrib import admin
from .models import Venue
from .models import Event
from .models import MyClubUser
from django.contrib.auth.models import Group
# Register your models here.

# admin.site.register(Venue,VenueAdmin)
admin.site.register(MyClubUser)

# Remove Groups
admin.site.unregister(Group)

# admin.site.register(Event)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'zip_code')
    ordering = ('name',)
    search_fields = ('name', 'address')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'event_date',
              'description', 'manager', 'approved')
    list_display = ('name', 'event_date', 'venue')
    list_filter = ('event_date', 'venue')
    ordering = ('-event_date',)
