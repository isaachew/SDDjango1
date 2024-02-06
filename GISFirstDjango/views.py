from django.shortcuts import render
from .models import Person

def splash(request):
    name = 'Isaac'
    people = Person.objects.filter(age__gte=20)
    debug_people = list(people)
    return render(request, "splash.html", {'name': name,'people':people})