#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：MxOnline -> YunPian
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/6/25 8:38
@Desc   ：发送短信验证码
==================================================
"""
import requests
import json


def send_single_sms(apikey, code, mobile):
    # 发送单条短信
    url = 'https://sms.yunpian.com/v2/sms/single_send.json'
    text = '【蜗犇AI】您的验证码是{}'.format(code)
    res = requests.post(url, data={
        'apikey': apikey,
        'mobile': mobile,
        'text': text
    })
    re_json = json.loads(res.text)
    return re_json


if __name__ == '__main__':
    res = send_single_sms('e3a4560f4769ffef24077aa73ec8498f', '1234','18468120158')
    import json
    res_json = json.loads(res.text)
    code = res_json['code']
    msg = res_json['msg']
    if code == 0:
        print('发送成功')
    else:
        print('发送失败：{}'.format(msg))