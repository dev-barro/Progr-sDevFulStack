from  django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index') # on indique  notre fonction index dans le views
]