from django.db import models
from employermodule import *
from employermodule.models import emplor_postjob, emplor_reg
import datetime
# Create your models here.


class seeker_img(models.Model):
    id = models.BigAutoField(primary_key=True)
    simg=models.CharField(max_length=150)


class seeker_resum(models.Model):
    id = models.BigAutoField(primary_key=True)
    stitle=models.CharField(max_length=100)
    sskill1=models.CharField(max_length=50)
    sskill2=models.CharField(max_length=50)
    sskill3=models.CharField(max_length=50)
    sskill4=models.CharField(max_length=50)
    sabout=models.CharField(max_length=150)
    sschoolname=models.CharField(max_length=50)
    squalification=models.CharField(max_length=50)
    scompany=models.CharField(max_length=50)
    srole=models.CharField(max_length=50)
    sstartdate=models.CharField(max_length=20)
    senddate=models.CharField(max_length=20)
    


class seeker_reg(models.Model):
    id = models.BigAutoField(primary_key=True)
    sfirstname=models.CharField(max_length=50)
    slastname=models.CharField(max_length=50,null=True)
    semail=models.CharField(max_length=50)
    spassword=models.CharField(max_length=100)
    smobilenumber=models.CharField(max_length=100)
    seekerid=models.ForeignKey(seeker_resum,on_delete=models.CASCADE,null=True)
    imgid=models.ForeignKey(seeker_img,on_delete=models.CASCADE,null=True)
   



class applyjob(models.Model):

    id = models.BigAutoField(primary_key=True)
    employer=models.CharField(max_length=150,null=True)
    seeker=models.CharField(max_length=150,null=True)
    jobid=models.CharField(max_length=150,null=True)

class blog_se(models.Model):

    id = models.BigAutoField(primary_key=True)
    imgblog=models.CharField(max_length=200,null=True)
    jobtext=models.CharField(max_length=1500,null=True)
    employerblog=models.CharField(max_length=150,null=True)
    seekerblog=models.CharField(max_length=150,null=True)
    date=models.DateField(auto_now_add=True,null=True)

class contact_us(models.Model):

    id = models.BigAutoField(primary_key=True)
    cname=models.CharField(max_length=200,null=True)
    cemail=models.CharField(max_length=1500,null=True)
    cphone=models.CharField(max_length=150,null=True)
    cmessage=models.CharField(max_length=150,null=True)
    seeker=models.CharField(max_length=150,null=True)
