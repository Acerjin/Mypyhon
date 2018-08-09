from django.shortcuts import render, redirect, HttpResponse
from rbac.models import UserInfo
from rbac.service.init_permission import init_permission
from .forms import  UserInfoModelForm
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate

def login(request):
    if request.method == "GET":
        return render(request, "rbac/login.html")
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print (username,password)
        user_obj = authenticate(username=username,password=password)

        print(user_obj)
        if not user_obj:
            return render(request, "rbac/login.html", {'error': '用户名或密码错误！'})
        else:
            init_permission(request, user_obj) #调用init_permission，初始化权限
            return redirect('/rbac/')

from django.shortcuts import render, redirect, reverse
from .models import UserInfo, Role, Permission, Menu
from .forms import UserInfoModelForm, RoleModelForm, PermissionModelForm, MenuModelForm


def index(request): # 提供后台管理的入口
    return render(request, 'rbac/index.html')


def users(request):
    """查询所有用户信息"""
    user_list = UserInfo.objects.all()
    return render(request, 'rbac/users.html', {'user_list': user_list})


def users_new(request):
    if request.method =="GET":
        # 传入ModelForm对象
        model_form = UserInfoModelForm()
        return render(request, 'rbac/common_edit.html', {'model_form': model_form, 'title': '新增用户'})
    else:
        model_form = UserInfoModelForm(request.POST)
        if model_form.is_valid():
            model_form.save()
            return redirect(reverse(users))
        else:
            return render(request, 'rbac/common_edit.html',{'model_form': model_form, 'title': '新增用户'})


def users_edit(request,id):
    user_obj = UserInfo.objects.filter(id=id).first()
    if request.method == 'GET':
        model_form = UserInfoModelForm(instance=user_obj)
        return render(request, 'rbac/common_edit.html', {'model_form': model_form, 'title': '编辑用户'})
    else:
        model_form = UserInfoModelForm(request.POST, instance=user_obj)
        if model_form.is_valid():
            model_form.save()
            return redirect(reverse(users))
        else:
            return render(request, 'rbac/common_edit.html', {'model_form': model_form, 'title': '编辑用户'})


def users_delete(request, id):
    user_obj = UserInfo.objects.filter(id=id).first()
    user_obj.delete()
    return redirect(reverse(users))
