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


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=2)
    password = forms.CharField(required=True, min_length=3)

