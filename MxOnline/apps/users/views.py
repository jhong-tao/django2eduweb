from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse

from apps.users.forms import LoginForm

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        # 表单验证
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 通过用户名和密码查询用户是否存在
            user_name = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=user_name, password=password)
            if user is not None:
                # 查询到用户
                login(request, user)
                # 登录成功后返回页面
                # 1.产生cookies和session
                return HttpResponseRedirect(reverse('index'))
            else:
                # 未查询到用户
                return render(request, 'login.html', {'msg': '用户名或密码错误', 'login_form':login_form})
        else:
            return render(request, 'login.html', {'login_form':login_form, 'msg':'用户名或者密码错误'})
