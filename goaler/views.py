# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('measurement_tracker:history'))
    else:
        return render(request, 'goaler/index.html')


def home_files(request, filename):
    return render(request, filename, {}, content_type='text/plain')
