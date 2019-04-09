from django.urls import path

from server.pages.views import index
from . import views
# Place your URLs here:

app_name = 'accounts'
urlpatterns = [
    path('tenantuser/:id/change_password', views.changePassword, name='change_password'),
]
