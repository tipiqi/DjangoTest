#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Darkoqi
# datetime:2020/8/24 13:46
# software: PyCharm

from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views

app_name = "account"
urlpatterns = [
    # url(r"^$",views.blog_articles,name="blog_title")
    path('', views.user_login, name="user_login"),
    # path('', auth_views.LoginView.as_view(), name="user_login"),
    # url(r'(?P<articles_id>\d)/$', views.blog_articles, name="blog_articles"),
    url(r'^register/$', views.register, name="user_register")
]
