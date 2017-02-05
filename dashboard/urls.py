# -*- coding: utf-8 -*-
"""
    notification.urls
    ~~~~~~~~~~~~~~~~~
    :copyright: Copyright 2017 by The Air-Child Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""

from django.conf.urls import url
from . import views

app_name = 'dashboard'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]
