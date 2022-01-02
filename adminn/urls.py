
from django.urls import include, path
from . import views
urlpatterns = [
    path('admin/',views.emplyad,name='employad'),
    path('em_ad/',views.emad,name='emrad'),
    path('job_tb/',views.jbtb,name='jbtb'),

    path('deletese/<int:sid>/',views.deletesc,name='deletese'),
    path('deleteem/<int:emid>/',views.deleteem,name='deleteem'),
  
   path('deletejob/<int:jobid>/',views.deletejob,name='deletejob'),
]
