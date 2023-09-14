

from . import views
from django.urls import path

urlpatterns = [

   path('',views.demo,name='demo'),
   # path('',views.operations,name='operations'),
   # path('opera/',views.addition,name='addition'),
]