"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt        # 去除crsf验证
import xadmin

from apps.users.views import LoginView, LogoutView, SendSmsView, DynamicLoginView,RegisterView

# url = 'http://127.0.0.1:8000  '

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),       # ''代表了网站根目录 url
    # path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('d_login/', DynamicLoginView.as_view(), name='d_login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^send_sms/', csrf_exempt(SendSmsView.as_view()), name='send_sms'),
]

# 1.CBV(class base view) FBV(fanctiong base view)

# 编写一个view的步骤
"""
1. view 代码
2. 配置url
3. 修改html中访问的相关地址
"""

