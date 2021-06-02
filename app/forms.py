from app.models import Sheet
from django import forms
from django.forms import Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2','email']
        widgets={
            'username':forms.TextInput(attrs={'placeholder':'Enter UserName','class':'form-control','style':'width:100%'}),
            'password1':forms.TextInput(attrs={'placeholder':'Enter Password','class':'form-control','style':'width:100%'}),
            'password2':forms.PasswordInput(attrs={'placeholder':'Confirm Password','class':'form-control','style':'width:100%'}),
            'email':forms.TextInput(attrs={'placeholder':'Enter Email','class':'form-control','style':'width:100%'}),
        }

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"placeholder":"Enter UserName","class":"form-control","style":"width:100%"}))
    password=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={"placeholder":"Enter Password","class":"form-control","style":"width:100%"}))

class CreateSheetForm(forms.ModelForm):
    class Meta:
        model=Sheet
        fields='__all__'
        widgets={
            "name":forms.TextInput(attrs={'placeholder':'Enter a name for your sheet','class':'form-control','style':'width:100%'}),
            "rows":forms.NumberInput(attrs={'placeholder':'Enter no. of rows requried','class':'form-control','style':'width:100%'}),
            "colomns":forms.NumberInput(attrs={'placeholder':'Enter no. of colomns required','class':'form-control','style':'width:100%'})
        }