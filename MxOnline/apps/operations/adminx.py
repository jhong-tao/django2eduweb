#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：MxOnline -> adminx
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/6/23 9:20
@Desc   ：
==================================================
"""
import xadmin

from apps.operations.models import UserAsk, CourseComments, UserCourse, UserFavorite, UserMessage


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']
    # list_editable = ['lesson', 'name', 'add_time']


class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']
    # list_editable = ['lesson', 'name', 'add_time']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']
    # list_editable = ['lesson', 'name', 'add_time']


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'add_time']
    search_fields = ['user', 'fav_id']
    list_filter = ['user', 'fav_id', 'add_time']
    # list_editable = ['lesson', 'name', 'add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']
    # list_editable = ['lesson', 'name', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
