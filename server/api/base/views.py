from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser,  MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import list_route
from django.shortcuts import get_object_or_404
from server.tenants.models import Client
from server.accounts.models import TenantUser
from server.pages.models import Page, Order
from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    """
        list:
        Return a list of all the existing users.
        read:
        Return the given user.
        me:
        Return authenticated user.
    """
    queryset = TenantUser.objects.all()
    serializer_class = serializers.TenantUserSerializer

    def retrieve(self, request, pk=None):
        """
        If provided 'pk' is "me" then return the current user.
        """
        if request.user and pk == 'me':
            return Response(serializers.TenantUserSerializer(request.user).data)
        return super(UserViewSet, self).retrieve(request, pk)

    @list_route(methods=['put'], serializer_class=serializers.PasswordSerializer)
    def set_password(self, request):
        serializer = serializers.PasswordSerializer(data=request.data)

        if serializer.is_valid():
            user = request.user
            if not user.check_password(serializer.data.get('old_password')):
                return Response({'old_password': ['Wrong password.']},
                                status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            user.set_password(serializer.data.get('new_password'))
            user.save()
            return Response({'status': 'password set'}, status=status.HTTP_200_OK)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


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
        if self.action == 'list':
            # read single record
            return serializers.PageListSerializer
        elif self.action == 'create':
            return serializers.PageCreateSerializer
        else:
            return serializers.PageSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'retrieve':
            # get single page requires read permission
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        else:
            # others need to authentication
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, pk=None):
        """
        If pk is provided 'pk' as integer then query using Primary Key, otherwise use Slug field instead of Primary Key.
        """
        if not PageViewSet.is_integer(self, pk):
            queryset = Page.objects.all()
            page = get_object_or_404(queryset, slug=pk)
            serializer = serializers.PageSerializer(page)
            return Response(serializer.data)
        return super(PageViewSet, self).retrieve(request, pk)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        return serializer.save(updater=self.request.user)

    def is_integer(self, val):
        try:
            val = int(val)
            return True
        except ValueError:
            pass
            return False


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().filter()
    serializer_class = serializers.OrderSerializer
