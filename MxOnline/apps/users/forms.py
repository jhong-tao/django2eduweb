#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：MxOnline -> forms
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/6/24 21:35
@Desc   ：表单验证
==================================================
"""
from django import forms

from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    """
    用户名密码长度验证
    """
    username = forms.CharField(required=True, min_length=2)
    password = forms.CharField(required=True, min_length=3)


class DynamicLoginForm(forms.Form):
    """
    图像验证码
    """
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    captcha = CaptchaField()    # 图像验证码