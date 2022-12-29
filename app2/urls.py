from django.urls import path
from app2.views import *
app_name='something2'

urlpatterns=[
    path('jinja_tag1/',jinja_tag1,name='jinja_tag1')
]