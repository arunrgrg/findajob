
from cgitb import text
from contextlib import nullcontext
from django.shortcuts import render
from django.contrib import messages
from . models import *
from django.shortcuts import redirect
from django.http import JsonResponse
from random import random
from django.core.files.storage import FileSystemStorage
from usermodule.models import applyjob, seeker_img, seeker_reg, seeker_resum,blog_se
import datetime
from .forms import *

# pdf
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


def pdf(request,id=None):
    
    buf=io.BytesIO()
    c=canvas.Canvas(buf,pagesize=letter,bottomup=0)
    textob= c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",14)

    user=seeker_reg.objects.get(id=id)
    
    lines = [
        "        "+user.seekerid.stitle+"         ",
        "------------------------------------------",
        "                              ",
        "Full Name  :"+user.sfirstname,
        "                              ",
        "ABOUT   :"+user.seekerid.sabout,
        "                              ",
        "EMAIL  :"+user.semail,
        "                              ",
        "PHONE  :"+user.smobilenumber,
        "                              ",
        "============================",
        "                              ",
        "EDUCATION",
        "                              ",
        "SCHOOL NAME  :"+user.seekerid.sschoolname,
        "                              ",
        "QUALIFICATION  :"+user.seekerid.squalification,
        "                              ",
        "============================",
        "                              ",
        "EXPERIANCE",
        "                              ",
        "COMPANY  :"+user.seekerid.scompany,
        "                              ",
        "ROLE  :"+user.seekerid.srole,
        "                              ",
        "START/END DATE  :"+user.seekerid.sstartdate+" TO "+user.seekerid.senddate,
         "                              ",
        "============================",
        "                              ",
        "SKILL",
        "                              ",
        user.seekerid.sskill1,
        "                              ",
        user.seekerid.sskill2,
        "                              ",
        user.seekerid.sskill3,
        "                              ",
        user.seekerid.sskill4

    ]

    for line in lines:
        textob.textLine(line)
    
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf,as_attachment=True,filename='pdf.pdf')    



def employerhome(request):
    return render(request,'postjob.html')


def employerreg(request):
  
    form=employerval
    try:
        if request.method == "POST":
            form=employerval(request.POST)  
            
            if form.is_valid():

                companyname=form.cleaned_data['companyname']
                emailid=form.cleaned_data['emailid']
                epassword=form.cleaned_data['epassword']
                emobilenumber=form.cleaned_data['emobilenumber']            
                obj=emplor_reg.objects.filter(emailid=emailid).exists()    
                
                if obj==True:
                    messages.warning(request, 'This email address is already being used')
                else:
                    form.save()
                    return redirect('/signin/') 
                   
    except Exception as e:print(e)
    return render(request,'employerreg.html',{"form":form})


def employersign(request):
    try:
        if request.method == "POST":

           eemail = request.POST['er_email']
           epassword = request.POST['er_password']
           obj_sign = emplor_reg.objects.get(emailid = eemail)
           
           if obj_sign.epassword == epassword:
               
               request.session['emid'] = obj_sign.id
                       
               return redirect('/emplor_home/')
        
    except Exception as e:print(e)    
     
    return render(request,'employersignin.html')



def postjob(request):
    return render(request,'postjob.html')


def jobem(request):
    try:

        userid=request.session['emid']
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
               
            t=emplor_reg.objects.get(id=userid)
            p=em_img.objects.get(id=t.em_imgid_id)
            img1=p.eimg
                      
            sere=emplor_postjob(jobtitile=jobtitle,companyname=com_name,jobtype=jobtype,jobdescription=jobdesc,skill1=skill1,skill2=skill2,skill3=skill3,skill4=skill4,jobcategory=jobcategory,experiance=experience,qualification=qualification,salary=salary,location=p_location,employerid_id=userid,companyimage=img1)
            sere.save()
                
            return JsonResponse({"msg":"insert succesfully"})  
                    
    except Exception as e:print(e)  
    return redirect('/em_deta/')   


def emprof(request):
    return render(request,'emplorprofile.html')


def jobapp(request):

    employer=request.session['emid']
    obj = applyjob.objects.filter(employer=employer).values_list('seeker',flat=True)
    obj1=list(obj)
   
    em =seeker_reg.objects.filter(id__in=obj1).exclude()  
    seekrimg=''
   
    return render(request,'jobapp.html',{"user":em,"img":seekrimg})


def jobseekerp(request,sep):

    try:
        
        seekerrg=seeker_reg.objects.get(id=sep)
        seekerresm=seeker_resum.objects.get(id=seekerrg.seekerid_id)
        obimg = seeker_img.objects.get(id=seekerrg.imgid_id)

    except:

        obimg=''
        seekerresm=''
        seekerrg=''

    return render(request,'seekerprofile.html',{'userob':seekerresm,"user":seekerrg,"img":obimg})



def jobpost(request):

    try:

        userid=request.session['emid']
        employerjb=emplor_postjob.objects.filter(employerid_id=userid).values()
        e=emplor_reg.objects.get(id=userid)
        obimg=em_img.objects.get(id=e.em_imgid_id)
    except:

        obimg=''
        e=''

 
    return render(request,'viewjbpst.html',{"emplor":employerjb,"img":obimg})



def emresm(request):

    userid=request.session['emid']
    
    try:
        if request.method=="POST":

            ecname=request.POST['ecname']
            ecemail=request.POST['ecemail']
            ecmobilenumber=request.POST['ecmobilenumber']
            ecaddress=request.POST['ecaddress']
            ecwebsite=request.POST['ecwebsite']
            ecabout=request.POST['ecabout']
            
                 
            user=emplor_cmre(ecname=ecname,ecemail=ecemail,ecmobilenumber=ecmobilenumber,ecaddress=ecaddress,ecwebsite=ecwebsite,ecabout=ecabout)
            user.save()     
            userid=request.session['emid']
            emplor_reg.objects.filter(id=userid).update(em_reid=user.id)
           
    except Exception as e:print(e)
    return render(request,'cmresume.html')                   



def emimg(request):

     img=request.FILES['emimg']
     img_name=str(random())+img.name
     obj1=FileSystemStorage()
     obj1.save(img_name,img)
     obj2=em_img(eimg=img_name)
     obj2.save()
      
     userid=request.session['emid']
     emplor_reg.objects.filter(id=userid).update(em_imgid_id=obj2.id)
     jobimg=emplor_postjob.objects.filter(employerid_id=userid).update(companyimage=img_name)
     return render(request,'cmresume.html')  



def emsett(request):

    try:
        userid=request.session['emid']
        e=emplor_reg.objects.get(id=userid)
        obimg=em_img.objects.get(id=e.em_imgid_id)
        s_ob=emplor_cmre.objects.get(id=e.em_reid_id)

    except:
        s_ob=''
        obimg=''
        pass
    
    return render(request,'settingsbase.html',{"userob":s_ob,"img":obimg})       


def detachng(request):

    userid=request.session['emid']
    e=emplor_reg.objects.get(id=userid)
    
    f=emplor_reg.objects.get(id=userid)
    try:
        obimg=em_img.objects.get(id=e.em_imgid_id)
        s_ob=emplor_cmre.objects.get(id=f.em_reid_id)
    except:

        obimg=''
        s_ob=''

    try:
         if request.method=="POST":

              img=request.FILES['emimg']
              img_name=str(random())+img.name
              obj1=FileSystemStorage()
              obj1.save(img_name,img)
              em_img.objects.filter(id=f.em_imgid_id).update(eimg=img_name)
              jobimg=emplor_postjob.objects.filter(employerid_id=userid).update(companyimage=img_name)
    
    except Exception as e:print(e)
    return render(request,'editcmdet.html',{"userob":s_ob,"img":obimg})



def emajax(request):

    try:
        userid=request.session['emid']
        if request.method=="POST":
 
            ecname=request.POST['ecname']
            ecemail=request.POST['ecemail']
            ecmobilenumber=request.POST['ecmobilenumber']
            ecaddress=request.POST['ecaddress']
            ecwebsite=request.POST['ecwebsite']
            ecabout=request.POST['ecabout']

            p=emplor_reg.objects.get(id=userid)   
            sere=emplor_cmre.objects.filter(id=p.em_reid_id).update(ecname=ecname,ecemail=ecemail,ecmobilenumber=ecmobilenumber,ecaddress=ecaddress,ecwebsite=ecwebsite,ecabout=ecabout)
            return JsonResponse({"msg":"insert succesfully"})  
                    
    except Exception as e:print(e)  
    return redirect('/em_deta/')   



def chcmpwd(request):
     
     try:
         userid=request.session['emid']
         
         if request.method=="POST":

            cupwd=request.POST['ecupwd']
            newpassword=request.POST['enewpassword']

            obj=emplor_reg.objects.filter(epassword=cupwd).exists()

            if obj==True:
                seid=emplor_reg.objects.filter(id=userid).update(epassword=newpassword)
                return JsonResponse({"msg":"password change Successfully"})  

            else:
                return JsonResponse({"msg":"password incorrect"})  

     except Exception as e:print(e)

     return render(request,'emchngpwd.html')     


def chjbpst(request,id='default'):
    
    userid=request.session['emid']
    employerjb=emplor_postjob.objects.filter(employerid_id=userid).values()
    
    return render(request,'editjobpost.html',{"emplor":employerjb})     


def jbdet(request,**kwargs):

    jobdetail=kwargs.get('jbdid')
    jobdetails=emplor_postjob.objects.get(id=jobdetail)
    
    return render(request,'jobdetailsem.html',{"emplor":jobdetails}) 


def deletejb(request,**kwargs):

    jbid=kwargs.get('jbid')
    
    jbpst=emplor_postjob.objects.get(id=jbid)
    jbpst.delete()

    return redirect('/ch_post/')


def jobseeker(request):
    
    seeker=seeker_reg.objects.all()
    return render(request,'jobseekers.html',{"seeker":seeker})


def msg(request):
    
    em=request.session['emid']
                                                                                                                                                          
    if request.method=="POST":
      
        mail=request.POST['memail']
        message=request.POST['mmsg']
        seeker=request.POST['semid']
        h=int(seeker)
        d = datetime.datetime.today().replace(microsecond=0)
             
        mail1=mail_msg(email=mail,message=message,date=d,seeker=h,employer=em)
        mail1.save()
   
    return redirect('/jobapp/')


def blogem(request):

    userid=request.session['emid'] 
    s_ob=emplor_cmre.objects.get(id=userid)

    if request.method=="POST":

        blogimg=request.FILES['blogimg']
        img_name=str(random())+blogimg.name
        obj1=FileSystemStorage()
        obj1.save(img_name,blogimg)

        blogtext=request.POST['sblog']
        
        employernm=emplor_reg.objects.get(id=userid)
        nm=employernm.companyname
        blog=blog_se(imgblog=img_name,jobtext=blogtext,seekerblog=nm)
        blog.save()
    
    blog=blog_se.objects.all()
    return render(request,'blogem.html',{"blog":blog,"userob":s_ob})


def posts_edit(request, id=None):
    
    a=id   
    detail=emplor_postjob.objects.get(id=a)
    
    return render(request,'editjobid.html',{"detail":detail})



def posts_up(request):

    userid=request.session['emid'] 
    try:

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
    except Exception as e:print(e)
    return render(request,'editjobid.html')




def elogout(request):
    try:
        del request.session['emid']

    except KeyError:
        pass
    return  redirect('/emplor_signin/')

    

