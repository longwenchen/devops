# -*- coding: utf-8 -*-
from django.shortcuts import render
import subprocess
from django.http import HttpResponse

# Create your views here.


def index(request):
    """ 首页: 显示文章列表
    """
    text = '欢迎您！'
    return render(request, 'deployment/index.html', locals())


def push(request):
    if request.POST:
        subprocess.Popen("/home/appuser/push.sh", shell=True).wait()
    return HttpResponse("OK")

