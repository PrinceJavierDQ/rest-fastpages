# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.


def index(request):
    """
    Main (or index) view.

    Returns rendered default page to the user.
    """
    return render(request, 'main_app/index.html')


def page(request):

    """
    Main (or index) view.

    Returns rendered default page to the user.
    """
    return render(request, 'pages/index.html')

