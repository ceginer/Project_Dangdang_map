from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def home(request):

    return render(request, 'base.html')

def login(request):

    if request.method == 'POST':
        아이디 = request.POST['username']
        비밀번호 = request.POST['password']

        user = auth.authenticate(request, username=아이디, password=비밀번호)

        if user is not None:
            print("회원가입된 사람이 아니겠죠")
            return redirect('/join')
        else:
            auth.login(request, user)
            return redirect('/')

    return render(request, 'login.html')

def join(request):

    print("join 실행!")
    if request.method == 'POST' :
        print("여기는 포스트요청")

        아이디 = request.POST['username']
        비밀번호 = request.POST['password1']
        
        User.objects.create_user(username=아이디, password=비밀번호)


        return redirect('/')


    print("join 마지막 부분")
    return render(request, 'join.html')

def logout(request):

    auth.logout(request)
    return redirect('/')