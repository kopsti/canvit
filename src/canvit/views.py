from django.shortcuts import redirect
from django.urls import reverse

def home_redirect(request):
    return redirect(reverse('home:home'))
