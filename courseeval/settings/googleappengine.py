# Google App Engine Settinsg
from courseeval.settings.common import *

DATABASES = {
    'default': {
        'ENGINE': 'google.appengine.ext.django.backends.rdbms',
        'INSTANCE': 'courseevaltest:cloud1',
        'NAME': 'courseeval',
    }
}