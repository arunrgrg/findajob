
from django.urls import path
from . import views
urlpatterns = [

    path('emplor_home/',views.employerhome,name='employerhm'),

    path('emplor_reg/',views.employerreg,name='employer'),
    path('emplor_signin/',views.employersign,name='employersign'),
    path('postjob',views.postjob,name='postjob'),
    path('emplor_pro',views.emprof,name='emprof'),
    path('jobapp',views.jobapp,name='jobapp'),
    path('jobpost',views.jobpost,name='jobpost'),
   


    path('emreum/',views.emresm,name='emresume'),
    path('em_settings',views.emsett,name='emsettings'),
    path('em_deta/',views.detachng,name='deatailch'),
    path('ch_pwd/',views.chcmpwd,name='chcmpwd'),
    
    path('ch_post/',views.chjbpst,name='chngjbpst'),
    path('deletejbpst/<int:jbid>/',views.deletejb,name='deletejb'),
    path('jobdeem/<int:jbdid>/',views.jbdet),

    path('ecimg/',views.emimg),
    path('emajax/',views.emajax),
    path('jobem/',views.jobem),

    path('job_seeker/<int:sep>/',views.jobseekerp,name='jobseekerp'),
   
    path('elogout/',views.elogout,name='elogout'),
   



]
