from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView


class UserRegisterView(CreateView):
    model = User
    template_name = 'users/registration.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('user:login')

