from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import UserForm, EditorForm
from .filters import SubmissionFilter
from runner import Runner
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'accounts/home.html')

@login_required(login_url='login')
def problem(request, pk):
    preloaded_text = None
    imports = None
    input_fetcher = None
    custom_test_case = None
    custom_test_case = request.POST.get('custom_text', None)
    testcases = None

    user = User.objects.get(id=pk)

    custom = False
    if custom_test_case != None and custom_test_case != '':
        custom = True
        with open('custom_testcases.txt', 'w') as file:
            file.write(custom_test_case)
  
    with open('preload_code.txt', 'r') as file:
        preloaded_text = file.readlines()
    with open('wrap_left.txt', 'r') as file:
        imports = file.readlines()
    with open('wrap_right.txt', 'r') as file:
        input_fetcher = file.readlines()
    
    imports = ('').join(imports)
    input_fetcher = ('').join(input_fetcher)
    preloaded_text = ('').join(preloaded_text)
    if request.method == 'POST':
        form = EditorForm(request.POST, initial={'text': preloaded_text})
        if form.is_valid():
            with open('snippets.py', 'w') as file:
                user_input = form.cleaned_data['text'].replace('\r', '')
                user_input = ('\n').join([imports, user_input, input_fetcher])
                file.write(user_input)
            
            form.instance.user = user
            form.instance.submission_language = 'python'
            
            runner = Runner().run(custom)
            if custom:
                testcases = [testcase[0] for testcase in Runner().read_custom_testcases()]
            else:
                testcases = [testcase[0] for testcase in Runner().read_testcases()]
            
            results_zip = []
            for index, run in enumerate(runner):
                results_zip.append([run[0], run[1], run[2], testcases[index]])
            context = {'form': form, 
                       'preloaded': form.cleaned_data['text'],
                       'results_zip': results_zip
                       }
            statuses = Snippet.get_status()
            status = statuses[0][0]
            for index, result in enumerate(results_zip):
                if result[2] == 'WRONG ANSWER' or result[2] == 'TIME LIMIT EXCEEDED':
                    status = statuses[1][0]
                    break
            form.instance.status = status
            form.save()
            return render(request, 'accounts/dashboard.html', context)
    form = EditorForm(initial={'text': preloaded_text})
    context = {'form':form, 'snippets': Snippet.objects.all()}
    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
def profile(request, pk):
    user = User.objects.get(id=pk)
    submissions = Snippet.objects.filter(user=user)
    
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

@login_required(login_url = 'login')
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

@login_required(login_url='login')
def viewSubmission(request, submission_id):
    submission = Snippet.objects.get(pk=submission_id)
    file_content = None
    with open('snippets.py', 'r') as file:
        file_content = file.read()

    context = {'submission': submission, 'file_content': file_content}
    return render(request, 'accounts/submission.html', context)

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

def preloaded_view(request):
    preloaded_text_file = 'preloaded_text.py'

    # Read the content of the file
    with open(preloaded_text_file, 'r') as file:
        preloaded_text = file.read()

    return render(request, 'dashboard.html', {'preloaded_text': preloaded_text})

# @login_required(login_url='login')
# def save_snippets(request):
#     form = EditorForm()
#     if request.method == 'POST':
#         form = EditorForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data['code'])
#         # snippets = request.POST.getlist('snippet')
#         # with open('snippets.py', 'w') as file:
#         #     for snippet in snippets:
#         #         file.write(snippet + '\n')
#         return HttpResponse('Snippets saved successfully!')
#     else:
#         return HttpResponse('Invalid request method.')

# def deleteUser(request, pk):
#     user = User.objects.get(username=pk)

#     context = {'user': user}
#     return render(request, 'accounts/delete.html', context)