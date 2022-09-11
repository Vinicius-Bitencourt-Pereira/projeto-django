from json import load
from pickletools import read_uint1

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Members


def index(request):
    my_members = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'my_members': my_members,
    }
    return HttpResponse(template.render(context, request))
