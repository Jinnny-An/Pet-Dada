from django import forms
from .models import *
from member.models import User as UserAb


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
        labels = {'pet_name':'펫이름', 'gender':'성별',
            'size':'분류', 'neutered':'중성화', 'pet_img':'펫프사'}

class UserAbForm(forms.ModelForm):
    class Meta:
        model = UserAb
        fields = ['username', 'first_name', 'email', 'profile_img', 'user_ph', 'last_name']
        labels = {'username' : 'ID', 'first_name' : '이름', 'email':'email', 'profile_img' : '프로필 사진', 'user_ph':'연락처', 'last_name' : '주소'}