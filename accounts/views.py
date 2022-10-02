from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import CreateUserForm
# Create your views here.
from django.urls import reverse_lazy


class CreateUserView(CreateView):
   template_name='registration/signup.html'
   form_class=CreateUserForm
   
   def get_success_url(self):
      return reverse_lazy('login')
      
   

