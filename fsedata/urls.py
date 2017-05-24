# -*- coding: utf-8 -*-
"""
    fsedata.urls
    ~~~~~~~~~~~~
    :copyright: Copyright 2017 by The Air-Child Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""

from django.conf.urls import url
from .views import setting

app_name = 'fsedata'

urlpatterns = [
    #url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^setting$', setting.SettingView.as_view(), name='setting'),
]
