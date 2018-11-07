# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from ideas.models import Idea


class IdeaAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_date', 'title')
    list_display_links = list_display
admin.site.register(Idea, IdeaAdmin)
