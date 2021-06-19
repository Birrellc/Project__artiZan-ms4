from django.shortcuts import render
from .models import ContactDetails

# Create your views here.


def contact(request):
    """ A view to show contact information """

    contact = ContactDetails.objects.all()

    context = {
        'contact': contact,
    }

    return render(request, 'contact/contact.html', context)