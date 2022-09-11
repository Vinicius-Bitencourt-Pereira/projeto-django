from pickletools import read_uint1

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Members


def index(request):
    my_members = Members.objects.all().values()
    output = ""
    for x in my_members:
        output += x['firstname']
    return HttpResponse(output)
