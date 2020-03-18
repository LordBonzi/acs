from django.contrib import admin
from .models import Door, Card, Guest, Reader, Access 

# Register your models here.
admin.site.register(Door)
admin.site.register(Card)
#admin.site.register(Guest)

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('GuestFirstName', 'GuestLastName', 'GuestID', 'GuestCode', 'GuestEmail', 'GuestCard', 'GuestAddedBy', 'CreatedOn')
    ordering = ('GuestFirstName',)
    search_fields = ('GuestFirstName', 'GuestLastName', 'GuestEmail', 'GuestAddedBy', 'CreatedOn')

admin.site.register(Reader)
admin.site.register(Access)

