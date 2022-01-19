
from django.urls import include, path
from . import views
urlpatterns = [
    path('admin/',views.emplyad,name='employad'),
    path('em_ad/',views.emad,name='emrad'),
    path('job_tb/',views.jbtb,name='jbtb'),

    path('deletese/<int:sid>/',views.deletesc,name='deletese'),
    path('deleteem/<int:emid>/',views.deleteem,name='deleteem'),
    path('contactad',views.contact,name='contactad'),


    path('editseeker/<str:id>/',views.seeker_edit),
    path('editseeker/',views.seeker_ad),

    path('editem/<str:id>/',views.em_edit),
    path('editem/',views.emed),

    path('editjb/<str:id>/',views.jb_edit),
    path('editjb/',views.eeditjob),


   path('deletejob/<int:jobid>/',views.deletejob,name='deletejob'),
]
