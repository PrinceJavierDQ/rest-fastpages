# rest specific configuration


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'server.accounts.serializers.CustomUserDetailsSerializer'
}



