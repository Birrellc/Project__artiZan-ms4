from django.db import models


class ContactDetails(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Details'
    label = models.CharField(max_length=254)
    email = models.CharField(max_length=254, blank=True)
    tel = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.label
