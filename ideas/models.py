    # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Idea(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.id)