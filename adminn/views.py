from django.shortcuts import render
from employermodule import models
from usermodule.models import *
from employermodule.models import emplor_postjob, emplor_reg
from django.shortcuts import redirect
from django.db.models import Count
# Create your views here.



def emplyad(request):

    seeker=seeker_reg.objects.all()
    count=seeker_reg.objects.all().count()
    
    if request.method=='POST':

        sfirstname = request.POST['sfirstname']
        slastname = request.POST['slastname']
        semail = request.POST['semail']
        spassword = request.POST['spassword']
        smobile= request.POST['smobile']

        b=seeker_reg(sfirstname=sfirstname, slastname = slastname ,semail=semail, spassword= spassword,smobilenumber=smobile)
        b.save()
        
        return redirect('/admin/')

     
    
    return render(request,'admin.html',{'seeker':seeker,"count":count})



def deletesc(request,**kwargs):

    sid=kwargs.get('sid')   
    seeker=seeker_reg.objects.get(id=sid)
    seeker.delete()

    return redirect('/admin/')



def emad(request):

    emplor=emplor_reg.objects.all()
    count=emplor_reg.objects.all().count()
    
    if request.method=='POST':
        
        companyname = request.POST['companyname']
        emailid = request.POST['emailid']
        epassword= request.POST['epassword']
        emobilenumber = request.POST['emobilenumber']

        q=emplor_reg(companyname=companyname,emailid=emailid,epassword=epassword,emobilenumber=emobilenumber)
        q.save()

        return redirect('/em_ad/')


    
    return render(request,'employers.html',{'emplor':emplor,"count":count})




def deleteem(request,**kwargs):

    emid=kwargs.get('emid')
  
    employer=emplor_reg.objects.get(id=emid)
    employer.delete()

    return redirect('/em_ad/')



def jbtb(request):

    job=emplor_postjob.objects.all()
    count=emplor_reg.objects.all().count()

    if request.method=="POST":
     
            jobtitle=request.POST['jobtitle']
            com_name=request.POST['com_name']
            p_location=request.POST['p_location']
            jobtype=request.POST['jobtype']
            jobdesc=request.POST['jobdesc']
            skill1=request.POST['skill1']
            skill2=request.POST['skill2']
            skill3=request.POST['skill3']
            skill4=request.POST['skill4']
            jobcategory=request.POST['jobcategories']
            experience=request.POST['experience']
            salary=request.POST['salary']
            qualification=request.POST['qualification']
               
            sere=emplor_postjob(jobtitile=jobtitle,companyname=com_name,jobtype=jobtype,jobdescription=jobdesc,skill1=skill1,skill2=skill2,skill3=skill3,skill4=skill4,jobcategory=jobcategory,experiance=experience,qualification=qualification,salary=salary,location=p_location)
            sere.save()

            return redirect('/job_tb/')

    return render(request,'jobtb.html',{'job':job,"count":count})



def contact(request):

    a=contact_us.objects.all()

    return render(request,'contactad.html',{"cn":a})


def seeker_edit(request, id=None):
    a=id   
    detail=seeker_reg.objects.get(id=a)
    print(id)
    

    return render(request,'editseeker.html',{"detail":detail})


def seeker_ad(request):

    if request.method=='POST':

        sfirstname = request.POST['sfirstname']
        slastname = request.POST['slastname']
        semail = request.POST['semail']
        spassword = request.POST['spassword']
        smobile= request.POST['smobile']
        id= request.POST['id']

        a=seeker_reg.objects.filter(id=id).update(sfirstname=sfirstname, slastname = slastname ,semail=semail, spassword= spassword,smobilenumber=smobile)
               
    return render(request,'editseeker.html')

def em_edit(request,id=None):

    a=id   
    detail=emplor_reg.objects.get(id=a)
    print(id)
    

    return render(request,'editemployer.html',{"detail":detail})

def emed(request):

    if request.method=='POST':

        companyname = request.POST['companyname']
        emailid = request.POST['emailid']
        epassword= request.POST['epassword']
        emobilenumber = request.POST['emobilenumber']      
        id= request.POST['id']

        v=emplor_reg.objects.filter(id=id).update(companyname=companyname,emailid=emailid,epassword=epassword,emobilenumber=emobilenumber)

    return render(request,'editemployer.html')




def jb_edit(request,id=None):

    a=id   
    detail=emplor_postjob.objects.get(id=a)
    print(id)
    
    return render(request,'jobedit.html',{"detail":detail})


def eeditjob(request):

    if request.method=="POST":

            jobtitle=request.POST['jobtitle']
            com_name=request.POST['com_name']
            p_location=request.POST['p_location']
            jobtype=request.POST['jobtype']
            jobdesc=request.POST['jobdesc']
            skill1=request.POST['skill1']
            skill2=request.POST['skill2']
            skill3=request.POST['skill3']
            skill4=request.POST['skill4']
            jobcategory=request.POST['jobcategories']
            experience=request.POST['experience']
            salary=request.POST['salary']
            qualification=request.POST['qualification']
            id=request.POST['id']

            emplor_postjob.objects.filter(id=id).update(jobtitile=jobtitle,companyname=com_name,jobtype=jobtype,jobdescription=jobdesc,skill1=skill1,skill2=skill2,skill3=skill3,skill4=skill4,jobcategory=jobcategory,experiance=experience,qualification=qualification,salary=salary,location=p_location)
            

    return render(request,'jobedit.html')



def deletejob(request,jobid):

    v=emplor_postjob.objects.get(id=jobid)

    v.delete()
    return redirect('/job_tb/')
    
    


