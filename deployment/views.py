# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
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
    from tasks import add
    result = add.delay(1, 2)
    return HttpResponse(result.get())