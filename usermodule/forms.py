from django import forms
from django.forms import fields
from . models import *
from django.core.exceptions import ValidationError
from django.forms import EmailField
from django.core.validators import RegexValidator

class seekerva(forms.ModelForm):

    sfirstname = forms.CharField(label="firstname",widget=forms.TextInput(attrs={'class':'form-control','rows':3}))
    slastname = forms.CharField(label="lastname",widget=forms.TextInput(attrs={'class':'form-control','rows':3}))
    semail = forms.EmailField(label="email",widget=forms.TextInput(attrs={'class':'form-control','rows':3}))
    spassword = forms.CharField(label="password",widget=forms.TextInput(attrs={'class':'form-control','rows':3}))
    smobilenumber = forms.CharField(validators=[RegexValidator(regex=r'^\+?1?\d{9,10}$', message="enter valid Phone number")])

    
    def clean(self):
        
        cleaned_data = super().clean()
        cc_myself = cleaned_data.get("sfirstname")
        email=cleaned_data.get("semail")
        password=cleaned_data.get("spassword")
        
        if len(cc_myself) < 4:
            self._errors['sfirstname'] = self.error_class([
                'Minimum 5 characters required'])
        
        
        def isEmailAddressValid( semail ):
           
           try:
               if seeker_reg.objects.filter(semail=email).exists():

                   self._errors['semail'] = self.error_class([
                   'email used'])               
               else:
                    EmailField().clean(semail)
                    return True
                   
           except ValidationError:
               return False
        if len(password)<8:
            self._errors['spassword'] = self.error_class([
                'Minimum 8 characters required'])

        
    class Meta:

        model=seeker_reg
        fields=('sfirstname','slastname','semail','spassword','smobilenumber')