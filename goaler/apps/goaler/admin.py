# -*- coding: utf-8 -*-
from django.contrib import admin

from . import models


@admin.register(models.UserProfile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('username', 'interaction')

    search_fields = ['user__username']
