from django import forms
from django.forms import fields
from . models import *
from django.core.exceptions import ValidationError
from django.forms import EmailField
from django.core.validators import RegexValidator

class employerval(forms.ModelForm):

    companyname = forms.CharField(label="companyname",widget=forms.TextInput(attrs={'class':'form-control mt-2','rows':3}))
    emailid = forms.EmailField(label="email",widget=forms.TextInput(attrs={'class':'form-control mt-2','rows':3}))
    epassword = forms.CharField(label="password",widget=forms.TextInput(attrs={'class':'form-control mt-2','rows':3}))    
    emobilenumber = forms.CharField(label="mobile number",validators=[RegexValidator(regex=r'^\+?1?\d{9,10}$', message="enter valid Phone number")],widget=forms.TextInput(attrs={'class':'form-control mb-4','rows':3}))

    
    
    def clean(self):
        
        cleaned_data = super().clean()
        cc_myself = cleaned_data.get("companyname")
        password = cleaned_data.get("epassword")
        if len(cc_myself) < 5:
            self._errors['companyname'] = self.error_class([
                'Minimum 5 characters required'])
        
        if len(password) < 8:
            self._errors['epassword'] = self.error_class([
                'Minimum 8 characters required'])
        
        
        def isEmailAddressValid( emailid ):
           
           try:
               EmailField().clean(emailid)
               return True
           
           except ValidationError:
               return False
        

    class Meta:

        
        model=emplor_reg
        fields=('companyname','emailid','epassword','emobilenumber')