from django.shortcuts import render
from .models import Person

def splash(request):
    name = 'Isaac'
    people = Person.objects.all()
    debug_people = list(people)
    return render(request, "splash.html", {'name': name})