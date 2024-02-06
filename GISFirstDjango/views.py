from django.shortcuts import render

def splash(request):
    name = 'Isaac'
    return render(request, "splash.html", {'name': name})