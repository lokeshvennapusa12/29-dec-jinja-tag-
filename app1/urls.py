from django.urls import path
from  app1.views import *
app_name='something1'

urlpatterns=[
    path('jinja_tag/',jinja_tag,name='jinja_tag')
]