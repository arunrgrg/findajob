from unicodedata import name
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from employermodule.views import msg
from . models import *
from django.contrib import messages
from django.shortcuts import redirect
from random import random
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from employermodule.models import *
from .filters import postjobfilter
import ast
from . forms import *
from django.core.mail import send_mail


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
    form=seekerva
    try:
        if request.method == "POST":
            form=seekerva(request.POST)
           
            if form.is_valid():

                sfirstname=form.cleaned_data['sfirstname']
                slname=form.cleaned_data['slastname']
                semail=form.cleaned_data['semail']
                spassword=form.cleaned_data['spassword']
                smobilenumber=form.cleaned_data['smobilenumber']
                       
                obj=seeker_reg.objects.filter(semail=semail).exists()

                if obj==True:

                    messages.warning(request, 'This email address is already being used')
                    
                else:
                    
                    frem='aruntest655@gmail.com'
                    to=[semail]
                    msg='Dear    '+sfirstname+'    Thank you for completing your registration with findajob. This email serves as a confirmation that your account is activated and that you are officially a part of the findajob family.Enjoy! Regards,The findajob team'

                          
                    send_mail(
                        'findajob',
                        msg,
                        frem,
                        to,
                    )

                    form.save()
                    return redirect('/signin/') 
                        
    except Exception as e:print(e)
    return render(request,'employeereg.html',{"form":form})


def seekerhm(request):
   
    userid=request.session['sid']
    obj=seeker_reg.objects.get(id=userid)

    jobview=emplor_postjob.objects.all()
    # obimg=em_img.objects.get(id=userid)
    obimg=''
    postjob = emplor_postjob.objects.all()
    myFilter = postjobfilter(request.GET,queryset=postjob)   
    postjob=myFilter.qs

    msg=mail_msg.objects.filter(seeker=userid)
   
    return render(request,'userhome.html',{"user":obj,"jobview":jobview,"img":obimg,"myFilter":myFilter,"msg":msg})


def viewjobd(request,**kwargs):
    
    userid=request.session['sid']
    jobdetail=kwargs.get('jbsid')
    jobdetails=emplor_postjob.objects.get(id=jobdetail)
    obj=seeker_reg.objects.get(id=userid)
    
    mail=[obj.semail]
    name=obj.sfirstname
    
    if request.method=='POST':
        
        jobid=request.POST['jobid']       
        seeker=request.session['sid']
        k=applyjob.objects.filter(jobid=jobid).filter(seeker=seeker).exists()

        if (k==False):

            emplor=emplor_postjob.objects.get(id=jobid)
            job=emplor.jobtitile
            emplor_id=emplor.employerid_id
            company=emplor.companyname

            objap=applyjob(employer=emplor_id,seeker=seeker,jobid=jobid)
            objap.save()
            frem='aruntest655@gmail.com'
            msg='Dear    '+name+'    job applied for succesfully  for the position '+job+'  at '+company
            send_mail(
                    'findajob',
                    msg,
                    frem,
                    mail,
                    )
            messages.success(request, 'applied successfully')

        else:
            messages.info(request, 'already applyed to this job')    
    
    return render(request,'jobdetails.html',{"emplor":jobdetails,"user":obj}) 


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
    seeker_reg.objects.filter(id=userid).update(imgid_id=obj2.id)
     
    return render(request,'addresume.html')
     

def prof(request):

    userid=request.session['sid']
    obj=seeker_reg.objects.get(id=userid)
    s=obj.seekerid_id

    try:
                     
        s_ob=seeker_resum.objects.get(id=s)
        obimg=seeker_img.objects.get(id=obj.imgid_id)
    
    except:
        s_ob=''
        obimg=''

    return render(request,'myprofileebase.html',{"user":obj,"userob":s_ob,"img":obimg})


def profed(request):

    userid=request.session['sid']
    obj=seeker_reg.objects.get(id=userid)
    s=obj.seekerid_id

    try:
        s_ob=seeker_resum.objects.get(id=s)
        obimg=seeker_img.objects.get(id=obj.imgid_id) 
    except:
        s_ob=''
        obimg=''
    
    try:
         if request.method=="POST":

              img=request.FILES['img']
              img_name=str(random())+img.name
              print(img_name)
              obj1=FileSystemStorage()
              obj1.save(img_name,img)

              seid=seeker_img.objects.filter(id=obj.imgid_id ).update(simg=img_name)
              
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

            obj=seeker_reg.objects.get(id=userid)
            s=obj.seekerid_id
            
            sere=seeker_resum.objects.filter(id=s).update(stitle=stitle,sskill1=sskill1,sskill2=sskill2,sskill3=sskill3,sskill4=sskill4,sabout=sabout,sschoolname=sschool, squalification= squalification,scompany=scompany,sstartdate=sstartdate,senddate=senddate,srole=srole)
            seid=seeker_reg.objects.filter(id=userid).update(semail=semail)
          
            return JsonResponse({"msg":"insert succesfully"})  
                    
    except Exception as e:print(e)  
    return redirect('/profile_edit/')   


def chpwd(request):

    try:
        userid=request.session['sid']
        obj=seeker_reg.objects.get(id=userid)
        
        try:
            obimg=seeker_img.objects.get(id=obj.imgid_id)
        except:
            obimg=''
        
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
    return render(request,'changepwd.html',{"user":obj,"img":obimg})


def jblist(request):
    
    userid=request.session['sid']
    obj=seeker_reg.objects.get(id=userid)
  
    jobview = emplor_postjob.objects.all()
    postjob = emplor_postjob.objects.all()

    myFilter = postjobfilter(request.GET,queryset=postjob) 
    postjob=myFilter.qs

    return render(request,'joblist.html',{"user":obj,"jobview":jobview,"myFilter":myFilter})


def cnus(request):

    userid = request.session['sid']
    obj = seeker_reg.objects.get(id=userid)
    b = obj.sfirstname
    
    if request.method == "POST":
         
         cname = request.POST['cname']
         cemail = request.POST['cemail']
         cphone = request.POST['cmobile']
         cmessage = request.POST['cmessage']

         a = contact_us(cname=cname,cemail=cemail,cphone=cphone,cmessage=cmessage,seeker=b)
         a.save()

    return render(request,'contactus.html',{"user":obj})


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
    
    try:
        obimg = em_img.objects.get(id=obj.imgid_id)
    except:
        obimg=''
    
    postjob = emplor_postjob.objects.all()
    myFilter = postjobfilter(request.GET,queryset=postjob)
    postjob=myFilter.qs
    a=cate
 
    category=emplor_postjob.objects.filter(jobcategory=a)
    myFilter1 = postjobfilter(request.GET,queryset=category)
    category=myFilter1.qs

    return render(request,'joblist.html',{"user":obj,"jobview":jobview,"img":obimg,"myFilter":myFilter,"se":myFilter1,"nm":a})


def blog(request):

    userid=request.session['sid']
    obj=seeker_reg.objects.get(id=userid)
    if request.method=="POST":

        blogimg=request.FILES['blogimg']
        img_name=str(random())+blogimg.name
        obj1=FileSystemStorage()
        obj1.save(img_name,blogimg)

        blogtext=request.POST['sblog']
        
        employernm=seeker_reg.objects.get(id=userid)
        nm=employernm.sfirstname
        blog=blog_se(imgblog=img_name,jobtext=blogtext,seekerblog=nm)
        blog.save()
    
    blog=blog_se.objects.all()
 
    return render(request,'blog.html',{"blog":blog,"user":obj})



def applied(request):

    try:
        userid=request.session['sid']
        obj=seeker_reg.objects.get(id=userid)
        obimg=seeker_img.objects.get(id=obj.imgid_id)
        userid=request.session['sid']
        jb=applyjob.objects.filter(seeker=userid).values_list('jobid', flat=True)
        obj1=list(jb)
        app=emplor_postjob.objects.filter(id__in=obj1).exclude()
    
    except:
        app=''
        obimg=''
        pass

    return render(request,'appliedjb.html',{'app':app,"img":obimg})


def logout(request):
    try:
        del request.session['sid']

    except KeyError:
        pass
    return  redirect('/signreg/')

  

