#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Darkoqi
# datetime:2020/8/24 13:46
# software: PyCharm

from django.conf.urls import url
from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    # url(r"^$",views.blog_articles,name="blog_title")
    path('', views.blog_title, name="blog_title"),
    url(r'(?P<articles_id>\d)/$', views.blog_articles, name="blog_articles"),
]
