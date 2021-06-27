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
import redis

from MxOnline.settings import REDIS_HOST, REDIS_PORT


class RegisterGetForm(forms.Form):
    captcha = CaptchaField()


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


class DynamicLoginPostForm(forms.Form):
    """
    动态登录手机号和短信验证码验证
    """
    mobile = forms.CharField(required=True, min_length=11, max_length=11)
    code = forms.CharField(required=True, min_length=4, max_length=4)

    def clean_code(self):
        mobile = self.data.get('mobile')
        code = self.cleaned_data['code']

        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, charset='utf-8', decode_responses=True)
        redis_code = r.get(str(mobile))
        if code != redis_code:
            raise forms.ValidationError('验证码不正确')
        return self.cleaned_data

    # def clean(self):
    #     """
    #     判断验证码输入是否正确
    #     :return:
    #     """
    #     mobile = self.cleaned_data['mobile']
    #     code = self.cleaned_data['code']
    #
    #     r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, charset='utf-8', decode_responses=True)
    #     redis_code = r.get(str(mobile))
    #     if code != redis_code:
    #         raise forms.ValidationError('验证码不正确')
    #     return self.cleaned_data
