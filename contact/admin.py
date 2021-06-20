from django.contrib import admin
from .models import ContactDetails

# Register your models here.


class AddressesAdmin(admin.ModelAdmin):
    list_display = (
        'label',
        'email',
        'tel',
    )
    ordering = ('label',)


admin.site.register(ContactDetails, AddressesAdmin)
