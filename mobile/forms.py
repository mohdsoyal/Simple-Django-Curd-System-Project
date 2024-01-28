from django import forms
from .models import Student

class studentreg(forms.ModelForm):
    class Meta:
        model =Student
        fields =['name','email','password','mobile','address']
        
        
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
            'mobile':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
        }