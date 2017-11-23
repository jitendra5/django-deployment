from django.shortcuts import render
from app1.forms import UserForm,UserProfileForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(password+" -->")
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("User not active!!")
        else:
            print("Last login attempt failed !!")
            print("Username {} and Password {}".format(username,password))
            return HttpResponse("Invalid login detais supplied!")
    else:
        return render(request,'app1/login.html',{})
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def indexview(request):
    return render(request,'app1/index.html')
def contactview(request):
    return render(request,'app1/contact.html')
def formview(request):
    regis=False
    if request.method == 'POST':
        form1=UserForm(request.POST)
        form2=UserProfileForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            print("Name: "+form1.cleaned_data['username'])
            print("Email: "+form1.cleaned_data['email'])
            print("Password:"+ form1.cleaned_data['password'])
            print("Website:"+ form2.cleaned_data['website'])
            form1.save(commit=True)
            profile=form2.save(commit=False)
            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
                profile.save()
                regis=True
        else:
            print(form1.errors, form2.errors)

    else:
        form1=UserForm()
        form2=UserProfileForm()
    return render(request,'app1/forms.html',{'form1': form1,'form2' : form2, 'registered':regis})
