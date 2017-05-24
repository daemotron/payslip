# -*- coding: utf-8 -*-
"""
    settings
    ~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2017 by The Stormrose Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""

from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class SettingView(TemplateView, LoginRequiredMixin):
    """
    Display the settings
    """
    template_name = 'fsedata/setting.html'
