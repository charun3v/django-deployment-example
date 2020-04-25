from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect #(for login page)
from . import forms
from .forms import NewUserForm, UserForm, UserProfileInfoForm


#for the login page
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def index(request):
    # return HttpResponse("Hello world")
    return render(request, 'KMIO_app1/index.html')


@login_required #so that only users who are loged in can logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def scheduler(request):
    return HttpResponse("This is the scheduler page")


def info(request):
    pinfo = forms.PatientInfo()

    if request.method == 'POST':
        pinfo = forms.PatientInfo(request.POST)

        if pinfo.is_valid():
            #DO SOMETHING
            print("Validation Success")
            print("NAME: "+ pinfo.cleaned_data['name'])
            print("Email: "+ pinfo.cleaned_data['email'])
            print("Text: "+ pinfo.cleaned_data['text'])

    return render(request, 'KMIO_app1/forms.html', {'pinfo': pinfo})


def patient_id(request):
    pid = NewUserForm()

    if request.method == "POST":
        pid = NewUserForm(request.POST)
        if pid.is_valid():
                #if form(pid) is valid while clicking the submit button - save the form and go back to the index page
            pid.save(commit=True)
            return index(request)
        else:
            print("Error: Invalid form")

    return render(request, 'KMIO_app1/forms.html', {'pid': pid})


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password) #hashing the password in this code
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user #sets the one to one relation with User

            if 'profile_pic' in request.FILES: #checking if the user has uploaded profile pic
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'KMIO_app1/registrations.html',
                                  {'user_form': user_form,
                                   'profile_form': profile_form,
                                   'registered': registered})





def user_login(request):
    if request.method =='POST':
        username = request.POST.get('username') #getting the username and password from login.html from the name tag
        password = request.POST.get('password')

        user = authenticate(username=username, password=password) #authentication by django automatically

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active!")
        else:
            print("Someone tried to login and failed")
            print(f'Username: {username} and password {password}')
            return HttpResponse("invalid login details")

    else:
        return render(request, 'KMIO_app1/login.html',{})



# Create your views here.
