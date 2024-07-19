from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegistrationForm


class UserRegisterView(CreateView):
    model = User
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('user:login')

