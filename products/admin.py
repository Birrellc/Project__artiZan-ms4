from django.contrib import admin
from .models import Art, Category

# Register your models here.


class ArtAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'artist',
        'category',
        'price',
        'height',
        'width',
        'image_path',
        'image',
        'sold'
    )

    order = ('sku',)


admin.site.register(Art, ArtAdmin)
admin.site.register(Category)
