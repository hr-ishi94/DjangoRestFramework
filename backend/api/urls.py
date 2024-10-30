from django.urls import path
from  . import views

urlpatterns = [
    path('',views.api_home,name='view_home')
]

