from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view which return the index page """

    return render(request, 'home/index.html')