from django.db import models


class Category(models.Model):
    """
    Category Model used to assign and search be category.
    """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Art(models.Model):
    """
    Art Model used to display Art products on website.
    """
    class Meta:
        verbose_name_plural = 'Art'

    name = models.CharField(max_length=254)
    sku = models.CharField(max_length=254)
    artist = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    height = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    width = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_path = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name
