from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from server.tenants.models import Client
from server.accounts.models import TenantUser
from server.pages.models import Page
from . import serializers

class UserViewSet(viewsets.ModelViewSet):
    queryset = TenantUser.objects.all()
    serializer_class = serializers.TenantUserSerializer

    def retrieve(self, request, pk=None):
        """
        If provided 'pk' is "me" then return the current user.
        """
        if request.user and pk == 'me':
            return Response(serializers.TenantUserSerializer(request.user).data)
        return super(UserViewSet, self).retrieve(request, pk)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().filter()
    serializer_class = serializers.ClientSerializer

    def retrieve(self, request, pk=None):
        """
        If provided 'pk' is "me" then return the current user tenant.
        """
        if request.user and pk == 'me':
            tenant = Client.objects.filter(owner=request.user)
            return Response(serializers.ClientSerializer(tenant).data)
        return super(ClientViewSet, self).retrieve(request, pk)


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = serializers.PageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


    def retrieve(self, request, pk=None):
        """
        If provided 'pk' is "me" then return the current user tenant.
        """
        if (not PageViewSet.isInteger(pk)):
            queryset = Page.objects.all()
            page = get_object_or_404(queryset, slug=pk)
            serializer = serializers.PageSerializer(page)
            return Response(serializer.data)
        return super(PageViewSet, self).retrieve(request, pk)

    def isInteger(val):
        try:
            val = int(val)
            return True
        except ValueError:
            pass
            return False

        return False

