from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django import forms
# Create your views here.

class SignUpView(generic.CreateView):

    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')  #all generic classbased views the urls are not loaded
                                            # when the file is imported,
                                            #so we have to use the lazy form of reverse to load
                                            # them later when they’re available.


