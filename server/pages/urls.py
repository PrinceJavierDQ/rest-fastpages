from django.urls import path

from server.pages.views import index
from . import views
# Place your URLs here:

app_name = 'pages'
urlpatterns = [
    path('', views.index, name='index'),
]
