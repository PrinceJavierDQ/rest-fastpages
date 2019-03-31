# -*- coding: utf-8 -*-

# Logging
# https://docs.djangoproject.com/en/1.11/topics/logging/

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'tenant_context': {
            '()': 'tenant_schemas.log.TenantContextFilter'
        },
    },
    'formatters': {
        'tenant_context': {
            'format': '[%(schema_name)s:%(domain_url)s] '
            '%(levelname)-7s %(asctime)s %(message)s',
        },
        'verbose': {
            'format': (
                '%(asctime)s [%(process)d] [%(levelname)s] '
                'pathname=%(pathname)s lineno=%(lineno)s '
                'funcname=%(funcName)s %(message)s'
            ),
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': '%(asctime)s [%(levelname)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'tenant_context',
            'filters': ['tenant_context'],
        },
        'console-verbose': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'security': {
            'handlers': ['console-verbose'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}
