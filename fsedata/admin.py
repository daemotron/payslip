# -*- coding: utf-8 -*-
"""
    fsedata.admin
    ~~~~~~~~~~~~~

    :copyright: Copyright 2017 by The Air-Child Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""
from django.contrib import admin
from .models import Setting, Month

admin.site.register(Setting)
admin.site.register(Month)
