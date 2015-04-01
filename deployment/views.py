# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import subprocess
import json

# Create your views here.


def index(request):

    text = request.POST.get("blogtitle", "")
    response_data = dict()

    response_data['result'] = 'Writing'
    response_data['message'] = text

    if request.is_ajax():
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return render(request, 'deployment/index.html', locals())


def push(request):
    # if request.POST:
    proc = subprocess.Popen("ipconfig", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    info = proc.communicate()
    return HttpResponse(info)

