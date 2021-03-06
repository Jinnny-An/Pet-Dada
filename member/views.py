from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth import get_user_model

#활성화함수위해
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes,force_str
from .tokens import member_activation_token

#messages 출력하기위해
from django.contrib import messages
from tkinter import Button, messagebox

def home(request):
    return HttpResponse('<u>Home</u>')



def back(request):
    return HttpResponse('<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><font size ="10"><p><hi><center><b><u>아래 사이트를 클릭 후 재로그인해주세요.</u><br> -Petdada- <br> <font size ="15"><a href="/member/login/">LOGIN</a>')   

#회원가입#

def signup(request):
    if request.method=="POST":
        if User.objects.filter(username=request.POST['username']).exists(): #아이디 중복 체크
             return render(request, 'member/signup_error.html')
        if request.POST['password1'] ==request.POST['password']:   
            print(request.POST)
            username=request.POST["username"] #아이디
            firstname=request.POST["user_name"] #이름
            password=request.POST["password"] #비밀번호
            lastname=request.POST["lastname"] #주소
            email=request.POST["email"] #이메일
            user_ph = request.POST["user_ph"] #핸드폰번호
    
            user=User.objects.create_user(username,email,password,user_ph=user_ph)
            user.last_name=lastname
            user.first_name=firstname
            user.is_active = False
            user.save()
            current_site = get_current_site(request) 
            message = render_to_string('member/activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': member_activation_token.make_token(user),
            })
            mail_title = "계정 본인확인 이메일"
            mail_to = request.POST["email"]
            email = EmailMessage(mail_title, message, to=[mail_to])
            email.send()
            return render(request,"member/signup2.html")
        else:
            return render(request,"member/signup3.html")  
    
    return render(request,"member/signup.html")


# 회원가입기능
# 이메일에 @ & . 없으면 안내해준다.
from django.core.exceptions import ValidationError

def validate_email(email):
    if not '@' in email or not '.' in email:
        raise ValidationError(("Invalid Email"), code = 'invalid')
    


# 로그인 #

def login(request):
    # 포스트 
    if request.method == 'POST':
        # 정보 가져와서 
        username = request.POST['username']
        password = request.POST['password']
        
        
        # 로그인
        user = auth.authenticate(request, username=username, password=password)
        print(user)

        # 성공
        if user is not None:
            auth.login(request, user)
            request.session['id'] = user.id
            return redirect('/main/pet_main/')
        # 실패
        else:
            return render(request, 'member/back.html')
            #return render(request, 'member/error.html',  {'error': 'username or password is incorrect.'}))
    else:
        return render(request, 'member/login.html')

# 로그아웃 #

def logout(request):
        auth.logout(request)
        # 메인
        return redirect('/main/pet_main/')



# 이메일 활성화(비활성화) #

def activate(request, uid64, token,*args, **kwargs):
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and member_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        return redirect("/member/login")
    else:
        return render(request, 'member/login.html', {'error' : '계정 활성화 오류'})

    return 

