from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from yezi_weibo.models import WBUser
from django.contrib.auth import authenticate, login, logout


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        is_exist = User.objects.filter(username=username)
        if password == password1 and not is_exist:
            # create_user会把密码生成哈希值，插进数据库，create插进去的数据密码是明文形式.
            WBUser.objects.create_user(username=username, password=password)
            return redirect('account:login')
        else:
            return HttpResponse('密码不一致或用户名已存在')
    return render(request, 'account/register.html')


def log_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('密码错误或用户名不存在')
    return render(request, 'account/login.html')


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')
