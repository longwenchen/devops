# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.


def index(request):
    """ 首页: 显示文章列表
    """
    text = '欢迎您！'
    return render(request, 'deployment/index.html', locals())
