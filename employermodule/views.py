

from django.shortcuts import render
from django.contrib import messages
from . models import *
from django.shortcuts import redirect
from django.http import JsonResponse
from random import random
from django.core.files.storage import FileSystemStorage
from usermodule.models import applyjob, seeker_img, seeker_reg, seeker_resum
from psycopg2.extras import NumericRange

def employerhome(request):
    return render(request,'postjob.html')



def employerreg(request):
  
    try:
        if request.method == "POST":

            eemail = request.POST['er_email']
            obj = emplor_reg.objects.filter(emailid = eemail).exists()

            if (obj == True):

                messages.warning(request, 'This email address is already being used')
            
            else:

                companyname = request.POST['er_firstname']
                eemail = request.POST['er_email']              
                epassword = request.POST['er_password']
                emobilenum = request.POST['er_mobile']
                            
                user = emplor_reg(companyname = companyname,emailid = eemail,epassword = epassword,emobilenumber = emobilenum)
                user.save()

                return redirect('/emplor_signin/') 
                        
    except Exception as e:print(e)
    return render(request,'employerreg.html')




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
            
            
            
            userid=request.session['emid']
            sere=emplor_postjob(jobtitile=jobtitle,companyname=com_name,jobtype=jobtype,jobdescription=jobdesc,skill1=skill1,skill2=skill2,skill3=skill3,skill4=skill4,jobcategory=jobcategory,experiance=experience,qualification=qualification,salary=salary,location=p_location,employerid_id=userid)
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
    print(obj1)
  

    em =seeker_reg.objects.filter(id__in=obj1).exclude()
    print(em)

    seekrimg=seeker_img.objects.all()
      
        


    

    return render(request,'jobapp.html',{"user":em,"img":seekrimg})

def jobseekerp(request,sep):

    seekerrg=seeker_reg.objects.get(id=sep)
    seekerresm=seeker_resum.objects.get(id=sep)
    obimg = em_img.objects.get(id=sep)

    



    return render(request,'seekerprofile.html',{'userob':seekerresm,"user":seekerrg,"img":obimg})










def jobpost(request):

    userid=request.session['emid']
    employerjb=emplor_postjob.objects.filter(employerid_id=userid).values()
    obimg=em_img.objects.get(id=userid)
      
    return render(request,'viewjbpst.html',{"emplor":employerjb,"img":obimg})




def emresm(request):

    userid=request.session['emid']
    obj=emplor_reg.objects.get(id=userid)

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
     print(img_name)
     obj1=FileSystemStorage()
     obj1.save(img_name,img)
     obj2=em_img(eimg=img_name)
     obj2.save()
     

     userid=request.session['emid']
     emplor_reg.objects.filter(id=userid).update(em_imgid=userid)
     jobimg=emplor_postjob.objects.filter(employerid_id=userid).update(companyimage=img_name)
     return render(request,'cmresume.html')  




def emsett(request):

    userid=request.session['emid']
  
    s_ob=emplor_cmre.objects.get(id=userid)

    obimg=em_img.objects.get(id=userid)

    return render(request,'settingsbase.html',{"userob":s_ob,"img":obimg})       





def detachng(request):

    userid=request.session['emid']
    
    s_ob=emplor_cmre.objects.get(id=userid)
    obimg=em_img.objects.get(id=userid)
    

    try:
         if request.method=="POST":

              img=request.FILES['emimg']
              img_name=str(random())+img.name
              print(img_name)
              obj1=FileSystemStorage()
              obj1.save(img_name,img)
              print(userid)
              em_img.objects.filter(id=userid).update(eimg=img_name)
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
            print(ecname)
            
            
            sere=emplor_cmre.objects.filter(id=userid).update(ecname=ecname,ecemail=ecemail,ecmobilenumber=ecmobilenumber,ecaddress=ecaddress,ecwebsite=ecwebsite,ecabout=ecabout)
            
          
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





def chjbpst(request):

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



def elogout(request):
    try:
        del request.session['emid']

    except KeyError:
        pass
    return  redirect('/emplor_signin/')

    

