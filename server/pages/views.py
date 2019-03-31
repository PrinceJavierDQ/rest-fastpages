from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request, slug):
    template = loader.get_template('pages/index.html')
    context = {
        'slug': slug,
    }
    return HttpResponse(template.render(context, request))
