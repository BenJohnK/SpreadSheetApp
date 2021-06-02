from io import SEEK_CUR
from app.models import Sheet
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .forms import RegistrationForm,LoginForm,CreateSheetForm
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout

# Create your views here.

class LoginView(TemplateView):
    template_name='app/login.html'
    form_class=LoginForm
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/home/')
            messages.info(request,"Invalid Username or Password")
        return redirect('/')
class RegisterView(TemplateView):
    template_name='app/register.html'
    form_class=RegistrationForm
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        self.context["form"]=form
        if form.is_valid():
            form.save()
            username=form.cleaned_data["username"]
            messages.success(request,"Account created for "+username)
            return redirect('/')
        return render(request,self.template_name,self.context)

class HomePage(TemplateView):
    template_name='app/index.html'
    context={}
    def get(self,request,*args,**kwargs):
        has_sheet=True
        try:
            sheet=Sheet.objects.get(user=request.user)
            self.context["sheet"]=sheet
            self.context["has_sheet"]=has_sheet
        except:
            has_sheet=False
            self.context["has_sheet"]=has_sheet
        return render(request,self.template_name,self.context) 

class CreateSheet(TemplateView):
    template_name='app/createsheet.html'
    form_class=CreateSheetForm
    context={}
    def get(self,request,*args,**kwargs):
        user=request.user
        form=self.form_class(initial={"user":user})
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        self.context["form"]=form
        if form.is_valid():
            print("form is valid")
            name=form.cleaned_data["name"]
            rows=form.cleaned_data["rows"]
            colomns=form.cleaned_data["colomns"]
            user=request.user
            Sheet.objects.create(name=name,rows=rows,colomns=colomns,user=user)
            return redirect('/home/')
        return render(request,self.template_name,self.context)

class UpdateSheet(TemplateView):
    template_name='app/createsheet.html'
    form_class=CreateSheetForm
    context={}
    def get(self,request,*args,**kwargs):
        sheet=Sheet.objects.get(user=request.user)
        form=self.form_class(instance=sheet)
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        sheet=Sheet.objects.get(user=request.user)
        form=self.form_class(request.POST,instance=sheet)
        if form.is_valid():
            name=form.cleaned_data["name"]
            rows=form.cleaned_data["rows"]
            colomns=form.cleaned_data["colomns"]
            sheet.name=name
            sheet.rows=rows
            sheet.colomns=colomns
            sheet.user=request.user
            sheet.save()
            return redirect('/home/')
        self.context["form"]=form
        return render(request,self.template_name,self.context)

class LogoutView(TemplateView):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('/')