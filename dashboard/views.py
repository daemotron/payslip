# -*- coding: utf-8 -*-
"""
    dashboard.views.index
    ~~~~~~~~~~~~~~~~~~~~~
    :copyright: Copyright 2017 by The Air-Child Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""

from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    """
    Display the application dashboard
    """
    template_name = 'dashboard/home.html'
