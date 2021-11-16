
from django.urls import path
from . import views
urlpatterns = [
    path('home',views.homefun,name='home'),
   
]
