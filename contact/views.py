from django.shortcuts import render
from .models import ContactDetails

# Create your views here.


def contact(request):
    """ A view to show contact information """

    contacts = ContactDetails.objects.all()

    context = {
        'contacts': contacts,
    }

    return render(request, 'contact/contact.html', context)