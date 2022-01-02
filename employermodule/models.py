from django.db import models

# Create your models here.



class em_img(models.Model):
    id = models.BigAutoField(primary_key=True)
    eimg=models.CharField(max_length=150)

class emplor_cmre(models.Model):
    id = models.BigAutoField(primary_key=True)
    ecname=models.CharField(max_length=100)
    ecemail=models.CharField(max_length=50)
    ecmobilenumber=models.CharField(max_length=50)
    ecaddress=models.CharField(max_length=50)
    ecwebsite=models.CharField(max_length=50)
    ecabout=models.CharField(max_length=150)
   



class emplor_reg(models.Model):

    companyname=models.CharField(max_length=50)
    emailid=models.CharField(max_length=50)
    epassword=models.CharField(max_length=50)
    emobilenumber=models.CharField(max_length=100)
    em_reid=models.ForeignKey(emplor_cmre,on_delete=models.CASCADE,null=True)
    em_imgid=models.ForeignKey(em_img,on_delete=models.CASCADE,null=True)
  
   


class emplor_postjob(models.Model):
    JOBTYPE = (
        ('full time','full time'),
        ('intern','intern'),
        ('part time', 'part time'),
    )
    LOCATION = (
        ('Andhra Pradesh','Andhra Pradesh'),
          ('Arunachal Pradesh','Arunachal Pradesh'),
          ('Assam','Assam'),
          ('Bihar','Bihar'),
          ('Chhattisgarh','Chhattisgarh'),
          ('Goa','Goa'),
          ('Gujarat','Gujarat'),
          ('Haryana','Haryana'),
          ('Himachal Pradesh','Himachal Pradesh'),
          ('Jharkhand','Jharkhand'),
          ('Karnataka','Karnataka'),
          ('Kerala','Kerala'),
          ('Madhya Pradesh','Madhya Pradesh'),
          ('Maharashtra','Maharashtra'),
          ('Manipur','Manipur'),
          ('Meghalaya','Meghalaya'),
          ('Mizoram','Mizoram'),
          ('Nagaland','Nagaland'),
          ('Odisha','Odisha'),
          ('Punjab','Punjab'),
          ('Rajasthan','Rajasthan'),
          ('Sikkim','Sikkim'),
          ('Tamil Nadu','Tamil Nadu'),
          ('Telangana','Telangana'),
          ('Tripura','Tripura'),
          ('Uttar Pradesh','Uttar Pradesh'),
          ('Uttarakhand','Uttarakhand'),
          ('West Bengal','West Bengal'),
          ('Andhra Pradesh','Andhra Pradesh'),

    )
    EXPERIANCE = (
        ('fresher','fresher'),
        ('1 year','1 year'),
        ('1 to 5 yea','1 to 5 yea'),
        ('5 to 10 year', '5 to 10 year'),
        ('10 to 20 year', '10 to 20 year'),
    )
    CATEGORY = (

         ('Real Estate','Real Estate'),
         ('sale/marketing','sale/marketing'),
         ('education/training','education/training'),
         ('healthcare','healthcare'),
         ('science','science'),
         ('Technologies','Technologies'),
         ('art/Design','art/Design'),
         ('food services','food services'),
        
    )
    
   
    id = models.BigAutoField(primary_key=True)
    jobtitile=models.CharField(max_length=100)
    companyname=models.CharField(max_length=100)
    jobtype=models.CharField(max_length=50,choices=JOBTYPE)
    jobdescription=models.CharField(max_length=1000)
    skill1=models.CharField(max_length=1000,null=True)
    skill2=models.CharField(max_length=1000,null=True)
    skill3=models.CharField(max_length=1000,null=True)
    skill4=models.CharField(max_length=1000,null=True)
    jobcategory=models.CharField(max_length=50,choices=CATEGORY,null=True)
    experiance=models.CharField(max_length=50,choices=EXPERIANCE)
    qualification=models.CharField(max_length=1000)
    salary=models.CharField(max_length=100)
    location=models.CharField(max_length=100,choices=LOCATION)
    companyimage=models.CharField(max_length=500,null=True)
    employerid=models.ForeignKey(emplor_reg,on_delete=models.CASCADE,null=True)
    class Meta:
        db_table='employermodule_emplor_postjob'
    
    def __str__(self):
        return self.get_jobcategory_display()