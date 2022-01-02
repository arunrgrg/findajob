from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from . models import *
from django.contrib import messages
from django.shortcuts import redirect
from random import random
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from employermodule.models import *
from .filters import postjobfilter
import ast

def homefun(request):

    return render(request,'home.html')



def signin(request):
    
    try:
        if request.method == "POST":

           semail = request.POST['email']
           spassword = request.POST['password']
           obj_sign = seeker_reg.objects.get(semail=semail)
           
           if obj_sign.spassword == spassword:
               
               request.session['sid'] = obj_sign.id
                       
               return redirect('/home/')
        
    except Exception as e:print(e)    
    return render(request,'home.html')   



def employeereg(request):
    
    try:
        if request.method == "POST":

            semail=request.POST['email']
            obj=seeker_reg.objects.filter(semail=semail).exists()

            if (obj==True):
                messages.warning(request, 'This email address is already being used')
            
            else:

                sfirstname=request.POST['firstname']
                slname=request.POST['lastname']
                semail=request.POST['email']
                spassword=request.POST['password']
                smobilenum=request.POST['mobilenum']
                     
                user=seeker_reg(sfirstname=sfirstname,slastname=slname,semail=semail,spassword=spassword,smobilenumber=smobilenum)
                user.save()

                return redirect('/signin/') 
               
            
    except Exception as e:print(e)
    return render(request,'employeereg.html')



def seekerhm(request):



    
    userid=request.session['sid']
    obj=seeker_reg.objects.get(id=userid)

    jobview=emplor_postjob.objects.all()
    obimg=em_img.objects.get(id=userid)

    postjob = emplor_postjob.objects.all()
    myFilter = postjobfilter(request.GET,queryset=postjob)   
    postjob=myFilter.qs
     


     
     
    return render(request,'userhome.html',{"user":obj,"jobview":jobview,"img":obimg,"myFilter":myFilter})



def viewjobd(request,**kwargs):
    
    
    jobdetail=kwargs.get('jbsid')
    jobdetails=emplor_postjob.objects.get(id=jobdetail)

    if request.method=='POST':
        
        jobid=request.POST['jobid']       
        seeker=request.session['sid']
        k=applyjob.objects.filter(jobid=jobid).filter(seeker=seeker).exists()

        if (k==False):

            emplor=emplor_postjob.objects.get(id=jobid)
            emplor_id=emplor.employerid_id
     

            objap=applyjob(employer=emplor_id,seeker=seeker,jobid=jobid)
            objap.save()
            messages.success(request, 'applied successfully')

        else:
            messages.info(request, 'already applyed to this job')

        


    
    return render(request,'jobdetails.html',{"emplor":jobdetails}) 




def seeresum(request):
    userid=request.session['sid']
    obj=seeker_reg.objects.get(id=userid)

    try:
        if request.method=="POST":

            stitle=request.POST['stitle']
            sskill1=request.POST['sskill1']
            sskill2=request.POST['sskill2']
            sskill3=request.POST['sskill3']
            sskill4=request.POST['sskill4']
            sabout=request.POST['sabout']
            sschoolname=request.POST['sschoolname']
            squalification=request.POST['squalification']
            srole=request.POST['srole']
            scompany=request.POST['scompany']
            sstartdate=request.POST['sstartdate']
            senddate=request.POST['senddate']
            
          
            user=seeker_resum(stitle=stitle,sskill1=sskill1,sskill2=sskill2,sskill3=sskill3,sskill4=sskill4,sabout=sabout,sschoolname=sschoolname, squalification= squalification,scompany=scompany,sstartdate=sstartdate,senddate=senddate,srole=srole)
            user.save()
            
            userid=request.session['sid']
            seid=seeker_reg.objects.filter(id=userid).update(seekerid_id=user.id)
           
    except Exception as e:print(e)
    return render(request,'addresume.html',{"user":obj})




def imgfn(request):

     img=request.FILES['seimg']
     img_name=str(random())+img.name
     print(img_name)
     obj1=FileSystemStorage()
     obj1.save(img_name,img)
     obj2=seeker_img(simg=img_name)
     obj2.save()
     obj3=seeker_img.objects.all()

     userid=request.session['sid']
     seeker_reg.objects.filter(id=userid).update(imgid_id=userid)
     
     return render(request,'addresume.html')
     


def prof(request):
    userid=request.session['sid']
    obj=seeker_reg.objects.get(id=userid)
    s_ob=seeker_resum.objects.get(id=userid)

    obimg=seeker_img.objects.get(id=userid)

    return render(request,'myprofileebase.html',{"user":obj,"userob":s_ob,"img":obimg})



def profed(request):

    userid=request.session['sid']
    obj=seeker_reg.objects.get(id=userid)
    s_ob=seeker_resum.objects.get(id=userid)
    obimg=seeker_img.objects.get(id=userid)

    try:
         if request.method=="POST":

              img=request.FILES['img']
              img_name=str(random())+img.name
              print(img_name)
              obj1=FileSystemStorage()
              obj1.save(img_name,img)
              seid=seeker_img.objects.filter(id=userid).update(simg=img_name)
              
    except Exception as e:print(e)
    return render(request,'myprofileedit.html',{"user":obj,"userob":s_ob,"img":obimg})




def ajaxtst(request):
    try:
        userid=request.session['sid']
        if request.method=="POST":
            
            sname=request.POST['name']
            semail=request.POST['email']
            sphone=request.POST['phone']
            stitle=request.POST['title']
            sskill1=request.POST['skill1']
            sskill2=request.POST['skill2']
            sskill3=request.POST['skill3']
            sskill4=request.POST['skill4']
            sschool=request.POST['school']
            squalification=request.POST['qualification']
            scompany=request.POST['company']
            srole=request.POST['role']
            sstartdate=request.POST['startdate']
            senddate=request.POST['enddate']
            sabout=request.POST['about']
            
            sere=seeker_resum.objects.filter(id=userid).update(stitle=stitle,sskill1=sskill1,sskill2=sskill2,sskill3=sskill3,sskill4=sskill4,sabout=sabout,sschoolname=sschool, squalification= squalification,scompany=scompany,sstartdate=sstartdate,senddate=senddate,srole=srole)
            seid=seeker_reg.objects.filter(id=userid).update(semail=semail)
          
            return JsonResponse({"msg":"insert succesfully"})  
                    
    except Exception as e:print(e)  
    return redirect('/profile_edit/')   



def chpwd(request):

    try:
         userid=request.session['sid']
         obj=seeker_reg.objects.get(id=userid)
         if request.method=="POST":

            cupwd=request.POST['cupwd']
            newpassword=request.POST['newpassword']

            obj=seeker_reg.objects.filter(spassword=cupwd).exists()

            if obj==True:
                seid=seeker_reg.objects.filter(id=userid).update(spassword=newpassword)
                return JsonResponse({"msg":"password change Successfully"})  

            else:
                return JsonResponse({"msg":"password incorrect"})  

    except Exception as e:print(e)

    return render(request,'changepwd.html',{"user":obj})



def jblist(request):
    
    userid=request.session['sid']
    obj=seeker_reg.objects.get(id=userid)
  

    jobview = emplor_postjob.objects.all()
    obimg = em_img.objects.get(id=userid)
    
    postjob = emplor_postjob.objects.all()

    myFilter = postjobfilter(request.GET,queryset=postjob)
     
    postjob=myFilter.qs

    return render(request,'joblist.html',{"user":obj,"jobview":jobview,"img":obimg,"myFilter":myFilter})




def cnus(request):
    userid=request.session['sid']
    obj=seeker_reg.objects.get(id=userid)
    return render(request,'contactus.html',{"user":obj})
# def emplylst(request):
#     return render(request,'employlist.html')    



def jobdtls(request):
    return render(request,'jobdetails.html')           
    




def jobsearch(request):

     postjob = emplor_postjob.objects.all()
     myFilter = postjobfilter(request.GET,queryset=postjob)   
     postjob=myFilter.qs



     return render(request,'jobs.html',{"myFilter":myFilter})


def jobapply(request):

    
    if request.method=="POST":


        jobid=request.POST['jobid']
        print(jobid)
        a=request.session['sid']
        print(a)

    
        return redirect('/viewjob/',jbsid=jobid)


def categorys(request,cate):
    
    userid=request.session['sid']
    obj=seeker_reg.objects.get(id=userid)
  

    jobview = emplor_postjob.objects.all()
    obimg = em_img.objects.get(id=userid)
    postjob = emplor_postjob.objects.all()
    myFilter = postjobfilter(request.GET,queryset=postjob)
    postjob=myFilter.qs
    
    a=cate
    print(type(a))
    category=emplor_postjob.objects.filter(jobcategory=a)
    myFilter1 = postjobfilter(request.GET,queryset=category)
    category=myFilter1.qs

    return render(request,'joblist.html',{"user":obj,"jobview":jobview,"img":obimg,"myFilter":myFilter,"se":myFilter1,"nm":a})






def logout(request):
    try:
        del request.session['sid']

    except KeyError:
        pass
    return  redirect('/signreg/')

    

