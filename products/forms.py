from django import forms
from .models import Art, Category
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):

    class Meta:
        model = Art
        fields = ('name', 'sku', 'artist',
                  'price', 'category',
                  'height', 'width', 'image',
                  'sold')

    image = forms.ImageField(label='image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border rounded-0'
