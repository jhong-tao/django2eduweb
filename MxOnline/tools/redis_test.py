#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：MxOnline -> redis_test
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/6/27 9:43
@Desc   ：
==================================================
"""

import redis
import time

r = redis.Redis(host='localhost', port=6379, db=0, charset='utf8', decode_responses=True)

r.set('mobile', '1234')
r.expire('mobile', 3)
time.sleep(1)
print(r.get('mobile'))

