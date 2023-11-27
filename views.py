from django.shortcuts import render, redirect ,HttpResponseRedirect
from .forms import SignUpForm, AdminCreationForm, EventsForm
from .models import Event, CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


def createUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('login')
        else:
            messages.error(request,'something is wrong..')
    else:
        form = SignUpForm()
    context = {'forms':form}
    return render(request,'signup.html',context)

def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
                username = request.POST.get('Username')
                password = request.POST.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    auth_login(request,user)
                    messages.success(request,'Logged in successfully!!')
                    return redirect('home')
                else:
                    messages.error(request,'please,Enter Valid password or username')
                    
        return render(request,'login.html',{})
    else:
        return redirect('home')

def home(request):
    return render(request,'home.html')

def Events(request):
    Events = Event.objects.all().order_by('-Date_and_Time')
    context = {'Events':Events}
    return render(request,'Event.html',context)

def Read_more(request,pk):
    Events = Event.objects.get(id=pk)
    context = {'Event':Events}
    return render(request,'showEvent.html',context)

def delete_Event(request,pk):
    Events = Event.objects.get(id=pk)
    Events.delete()
    messages.success(request,'Event Deleted')
    return redirect('home')

def delete_user(request,pk):
    user = CustomUser.objects.get(id=pk)
    user.delete()
    messages.success(request,'user Deleted')
    return redirect('home')


def update_Event(request,pk):
    Events = Event.objects.get(id=pk)
    form = EventsForm(request.POST or None,request.FILES or None,instance=Events)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'update_event.html',{'form':form})

def About(request):
    return render(request,'about.html')

def logout(request):
    auth_logout(request)
    messages.success(request,'Logout successfully!!')
    return HttpResponseRedirect('/login/')

def AddEvents(request):
    if request.method == 'POST':
        form = EventsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit = False)
            messages.success(request,'Event Added')
        else:
            messages.error(request,'Something wrong,try again..')
    else:
        form = EventsForm()
    context = {'forms':form}
    return render(request,'add_event.html',context)

def Dashboard(request):
    users = CustomUser.objects.all()
    return render(request,'index.html',{'users':users})



