from django.shortcuts import render
from employermodule import models
from usermodule.models import seeker_reg
from employermodule.models import emplor_postjob, emplor_reg
from django.shortcuts import redirect
# Create your views here.



def emplyad(request):

    seeker=seeker_reg.objects.all()  
    
    return render(request,'admin.html',{'seeker':seeker})



def deletesc(request,**kwargs):

    sid=kwargs.get('sid')   
    seeker=seeker_reg.objects.get(id=sid)
    seeker.delete()

    return redirect('/admin/')



def emad(request):
    emplor=emplor_reg.objects.all()
    
    return render(request,'employers.html',{'emplor':emplor})




def deleteem(request,**kwargs):

    emid=kwargs.get('emid')
  
    employer=emplor_reg.objects.get(id=emid)
    employer.delete()

    return redirect('/em_ad/')



def jbtb(request):

    job=emplor_postjob.objects.all()




    return render(request,'jobtb.html',{'job':job})


def deletejob(request,jobid):

    v=emplor_postjob.objects.get(id=jobid)

    v.delete()
    return redirect('/job_tb/')
    
    


