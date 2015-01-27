# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import subprocess

# Create your views here.


def index(request):
    """ 首页: 显示文章列表
    """
    text = '欢迎您！'
    return render(request, 'deployment/index.html', locals())


def push(request):
    # if request.POST:
    proc = subprocess.Popen(["/bin/bash", "/home/appuser/push.sh"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    info = proc.communicate()
    return HttpResponse(info)

