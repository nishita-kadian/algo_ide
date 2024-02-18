from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import UserForm, EditorForm
from .filters import SubmissionFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = EditorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EditorForm()
    context = {'form':form, 'snippets': Snippet.objects.all()}
    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
def profile(request, pk):
    user = User.objects.get(id=pk)
    submissions = Submission.objects.filter(user=user)
    
    submissionStatusFilter = SubmissionFilter(request.GET, queryset=submissions)
    submissions = submissionStatusFilter.qs
    # myFilter = SubmissionFilter()
    
    context = {'user': user, 
               'submissions' : submissions, 
               'submissionStatusFilter': submissionStatusFilter}
    return render(request, 'accounts/profile.html', context)

def createUser(request):
    if request.user.is_authenticated:
        return redirect('login')
    else:
        form = UserForm()
        if request.method == "POST":
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                # user = form.cleaned_data.get('username')
                # messages.success(request,'Account was created for' + user)
                return redirect('/')

        context = {'form': form}

        return render(request, 'accounts/profile_form.html', context)

login_required(login_url = 'login')
def updateUser(request, pk):
    # user = User.objects.get(username=pk)
    user = get_object_or_404(User, pk=pk)
    form = UserForm(instance=user)
    context = {'form': form}
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'accounts/profile_form.html', context)

# def registerPage(request):
#     form = CreateUserForm()
#     if request.method == "POST":
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return 

#     context = {'form': form}
#     return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=="POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            # print(username, password)
            user = authenticate(request, username=username, password=password)
            # print(user)
            if user is not None:
                login(request, user)
                return redirect('/')
            # else:
            #     messages.info(request, 'Username or password is incorrect')
        
        context = {}
        return render(request, 'accounts/login.html', context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')


# def deleteUser(request, pk):
#     user = User.objects.get(username=pk)

#     context = {'user': user}
#     return render(request, 'accounts/delete.html', context)