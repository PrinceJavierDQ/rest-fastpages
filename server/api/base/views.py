from rest_framework import viewsets
from rest_framework.parsers import JSONParser,  MultiPartParser, FormParser
from rest_framework.response import Response
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
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide extra actions.
    """
    queryset = Page.objects.all()
    serializer_class = serializers.PageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    parser_classes = (MultiPartParser, FormParser, )

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.PageSerializer
        else:
            return serializers.PageListSerializer

    def retrieve(self, request, pk=None):
        """
        If provided 'pk' is "me" then return the current user tenant.
        """
        if not PageViewSet.is_integer(self, pk):
            queryset = Page.objects.all()
            page = get_object_or_404(queryset, slug=pk)
            serializer = serializers.PageSerializer(page)
            return Response(serializer.data)
        return super(PageViewSet, self).retrieve(request, pk)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def is_integer(self, val):
        try:
            val = int(val)
            return True
        except ValueError:
            pass
            return False

