from django.contrib import admin
from .models import ContactDetails

# Register your models here.


class AddressesAdmin(admin.ModelAdmin):
    list_display = (
        'label',
        'email',
    )
    ordering = ('label',)


class NoticeAdmin(admin.ModelAdmin):
    list_display = (
        'notice',
    )


admin.site.register(ContactDetails, AddressesAdmin)
