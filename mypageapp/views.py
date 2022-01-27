from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *


def update_user(request):
    id = request.session['id']
    profile = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance = profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('mypageapp:update_user')
            # , id = id)
    else:
        try :
            pet = Pet.objects.get(user_id = id)
        except :
            pet = Pet.objects.filter(user_id = id)

        form = UserForm(instance = profile)
        return render(request, 'mypageapp/user_profile.html', {'form':form, 'pet':pet},
        )




# Q1해결. try/excetp 문 이용해서 한 계정에 pet 이 두 개 이상 등록되지 않도록.
def create_pet(request):
    id = request.session['id']
    if request.method=='POST':
        try :
            form = PetForm(request.POST, request.FILES)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = User.objects.get(id=id)
                profile.save()
                # print(profile.pet_img)
                return redirect('mypageapp:update_user', id = id)
            else:
                return HttpResponse('작성 양식이 잘못되었습니다.')
        except:
            return HttpResponse('이미 펫이 등록되어있습니다. 현재는 하나의 펫만 등록 가능합니다.')
    else:
        form = PetForm()
        return render(request, 'mypageapp/pet_profile.html', 
        {'form':form},
        )

def update_pet(request):
    id = request.session['id']
    profile = Pet.objects.get(user_id=id)
    profile.user = User.objects.get(id=id)
    if request.method=='POST':
        form = PetForm(request.POST, request.FILES, instance = profile)
        form.user = User.objects.get(id=id)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = form.user
            profile.save()
            return redirect('mypageapp:update_user')
    else:
        form = PetForm(instance = profile)
        return render(request, 'mypageapp/pet_profile.html', {'form':form},
        )


