# -*- coding: utf-8 -*-
"""
    fsedata.models.settings
    ~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2017 by The Air-Child Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""

from django.db import models


class Setting(models.Model):
    """
    Model class providing a registry-like key-value store for fsedata-related
    configuration information.
    """
    key = models.CharField(max_length=100, unique=True)
    value = models.CharField(max_length=200)
    description = models.CharField(max_length=255, blank=True)
