
from django.urls import path
from . import views
urlpatterns = [
    path('signreg/',views.homefun,name='home'),
    path('signin/',views.signin,name='seekersignin'),
    

    path('home/',views.seekerhm,name='seekerhm'),
    path('viewjob/<int:jbsid>/',views.viewjobd,name='viewjobd'),

    path('emply_reg/',views.employeereg,name='employee'),

    path('resume/',views.seeresum,name='seekerresume'),
    path('jobl_ist/',views.jblist,name='joblist'),
    path('contactus/',views.cnus,name='contactus'),
    path('blog/',views.blog,name='blog'),


    path('my_profile',views.prof,name='seemyprofile'),
    path('profile_edit/',views.profed,name='profileedit'),
    path('change_pwd/',views.chpwd,name='changepwd'),
    
    path('jobsearch/',views.jobsearch,name='jobsearch'),
    path('categorys/<str:cate>/',views.categorys,name='categorys'),

    path('applied/',views.applied,name='applied'),   
    
    path('job_deta',views.jobdtls,name='jobdetails'),
    path('logout',views.logout,name='logout'),
   


    path('simg/',views.imgfn),

    path('ajax/',views.ajaxtst)
]
