from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth import get_user_model
from .models import User


# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = get_user_model()
#         fields = ('username', 'email','last_name','first_name','profile_img','user_phone')


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email','last_name','first_name')   





# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = get_user_model()
#         fields = ('username', 'email','last_name','first_name')