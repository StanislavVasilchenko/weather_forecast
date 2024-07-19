from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    """Класс формы для отображения полей при регистрации пользователя"""
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)