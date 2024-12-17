from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import User

class CustomUserUpdate(UserChangeForm):
    password = None
    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'email',
        ]
class CustumUserCreationForm(UserCreationForm):
    class Meta:
        model = UserCreationForm
        fields = UserCreationForm.Meta.fields + ()