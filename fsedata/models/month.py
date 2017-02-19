# -*- coding: utf-8 -*-
"""
    fsedata.models.month
    ~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2017 by The Air-Child Project team, see AUTHORS.
    :license: MIT License, see LICENSE for details.
"""

from django.db import models
import datetime


class Month(models.Model):
    """
    Model class providing the time framework (month) for all FSE data
    with a monthly frequency.
    """
    month = models.PositiveIntegerField()
    year = models.PositiveIntegerField()

    def __str__(self):
        """
        Provide an understandable representation of a Month object

        :return: year-month string
        """
        dt = datetime.date(self.year, self.month, 1)
        return "{date} ({year}-{month:0>2d})".format(date=dt.strftime('%B %Y'), year=self.year, month=self.month)

    class Meta:
        """
        Meta class for the fsedata month
        """
        unique_together = (('year', 'month'))
        ordering = ['-year', '-month']
