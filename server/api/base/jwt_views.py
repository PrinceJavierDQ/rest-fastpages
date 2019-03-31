from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['email'] = user.email
        tenant = user.tenants.first()
        if tenant:
            token['api_url'] = tenant.domain_url
        else:
            token['api_url'] = ''

        # ...
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


token_obtain_pair = MyTokenObtainPairView.as_view()
