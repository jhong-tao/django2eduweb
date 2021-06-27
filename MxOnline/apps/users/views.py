from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
import redis

from apps.users.forms import LoginForm, DynamicLoginForm, DynamicLoginPostForm,RegisterGetForm
from apps.utils.YunPian import send_single_sms
from apps.utils.random_str import generate_random
from MxOnline.settings import yp_apikey, REDIS_HOST, REDIS_PORT
from apps.users.models import UserProfile


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        register_get_form = RegisterGetForm()
        return render(request, 'register.html', {
            'register_get_form': register_get_form
        })

    def post(self, request, *args, **kwargs):
        return render(request, 'register.html')


class DynamicLoginView(View):
    def post(self, request, *args, ** kwargs):
        dynamic_login = True        # 用来做登录方式判断
        login_form = DynamicLoginPostForm(request.POST )
        if login_form.is_valid():
            # 没有注册账号依然可以登录
            mobile = login_form.cleaned_data['mobile']
            existed_users = UserProfile.objects.filter(mobile=mobile)
            if existed_users:
                user = existed_users[0]
                # login(request, user)        # 用户存在直接登录产生cookies
            else:
                # 用户不存在，新建用户
                user = UserProfile(username=mobile)
                password = generate_random(10, 2)
                user.set_password(password)
                user.mobile = mobile
                user.save()
            login(request, user)    # 登录用户，产生cookies
            return HttpResponseRedirect(reverse('index'))       # 登录成功 跳转首页
        else:
            d_form = DynamicLoginForm()  # 图像验证码
            return render(request, 'login.html', {'login_form': login_form,
                                                  'dynamic_login': dynamic_login,
                                                  'd_form':d_form,
                                                  'msg': '电话号码或验证码错误'
                                                  })


class SendSmsView(View):
    def post(self, request, *args, **kwargs):
        re_dict = {}
        send_sms_form = DynamicLoginForm(request.POST)
        if send_sms_form.is_valid():
            mobile = send_sms_form.cleaned_data['mobile']
            # 随机生成数字验证码
            code = generate_random(4, 0)
            re_json = send_single_sms(apikey=yp_apikey, code=code, mobile=mobile)
            if re_json['code'] == 0:
                re_dict['status'] == 'success'
                r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, charset='utf8', decode_responses=True)
                r.set(str(mobile), code)
                r.expire(str(mobile), 60*5)     # 设置验证码5分钟过期
            else:
                re_dict['msg'] = re_json['msg']
        else:
            for key, value in send_sms_form.errors.items():
                re_dict[key] = value[0]
        return JsonResponse(re_dict)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)     # 退出，即删除或者让cookies超时
        return HttpResponseRedirect(reverse('index'))


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))

        login_form = DynamicLoginForm()     # 图像验证码
        return render(request, 'login.html', {
            'login_form': login_form
        })

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
                login(request, user)        # 生成cookies
                # 登录成功后返回页面
                # 1.产生cookies和session
                return HttpResponseRedirect(reverse('index'))
            else:
                # 未查询到用户
                return render(request, 'login.html', {'msg': '用户名或密码错误', 'login_form': login_form})
        else:
            return render(request, 'login.html', {'login_form': login_form, 'msg': '用户名或者密码错误'})
