#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：MxOnline -> random_str.py
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/6/25 15:59
@Desc   ：生成随机数
==================================================
"""
import string
from random import choice


def generate_random(random_length, type):
    """
    随机字符串生成函数
    :param random_length: 字符串长度
    :param type: 字符串类型（存数字，数字+字符串，数字+字符串+特殊字符）
    :return:
    """

    # 随机字符串种子
    if type == 0:
        random_seed = string.digits
    elif type == 1:
        random_seed = string.digits + string.ascii_letters
    elif type == 2:
        random_seed = string.digits + string.ascii_letters + string.punctuation
    random_str = []

    while (len(random_str) < random_length):
        random_str.append(choice(random_seed))
    return ''.join(random_str)


if __name__ == '__main__':
    print(generate_random(4, 0))
