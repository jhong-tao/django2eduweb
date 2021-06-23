#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：MxOnline -> adminx
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/6/23 8:21
@Desc   ：
==================================================
"""
import xadmin
from xadmin.views import BaseAdminView
from xadmin.views import CommAdminView

from apps.courses.models import Course, Lesson, Video, CourseResource


class GlobalSettings(object):
    site_title = '慕学后台管理系统'
    site_footer = '慕学在线网'


class BaseSettings(object):
    enable_themes = True
    user_bootswatch = True


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students']
    list_filter = ['name', 'teacher__name', 'desc', 'detail', 'degree', 'students']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students']
    list_editable = ['degree', 'desc']


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name', 'add_time']
    # list_editable = ['course', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']
    # list_editable = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name', 'add_time']
    # list_editable = ['lesson', 'name', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)

xadmin.site.register(CommAdminView, GlobalSettings)
xadmin.site.register(BaseAdminView, BaseSettings)
