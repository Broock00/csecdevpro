from django.shortcuts import render, redirect ,HttpResponseRedirect
from .forms import SignUpForm, EventsForm, Announcement
from .models import Event, CustomUser, SpecialAnnouncement
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

@login_required
def createUser(request):
    """ 
        - Handles user creation.
        - Renders the 'signup.html' template.
        - Supports both GET and POST requests.
        - If POST request is valid, a new user is created, and success/error messages are displayed.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User created successfully!!')
        else:
            messages.error(request,'something is wrong..')
    else:
        form = SignUpForm()
    context = {'forms':form}
    return render(request,'signup.html',context)

def login(request):
    """  
    - Handles user authentication.
    - Renders the 'login.html' template.
    - Redirects authenticated users to the home page.
    - Displays success/error messages based on authentication results.
    """
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
        """ 
        - Renders the 'home.html' template.
        - Simple view representing the home page.
        """
        Announcement = SpecialAnnouncement.objects.all().order_by('-date_time')
        return render(request,'home.html',{'announcement':Announcement})


def Events(request):
    """ 
    - Retrieves all events from the database, ordered by date and time.
    - Renders the 'Event.html' template with the retrieved events.
    """
    Events = Event.objects.all().order_by('Today')
    context = {'Events':Events}
    return render(request,'Event.html',context)

def Read_more(request,pk):
    """ 
    - Displays detailed information about a specific event.
    - Renders the 'showEvent.html' template with details of the selected event.
    """
    Events = Event.objects.get(id=pk)
    context = {'Event':Events}
    return render(request,'showEvent.html',context)

@login_required
def delete_Event(request,pk):
    """
    - Deletes a specific event from the database based on the provided primary key.
    - Displays a success message upon successful deletion.
    - only admin can do this
    """
    Events = Event.objects.get(id=pk)
    Events.delete()
    messages.success(request,'Event Deleted')
    return redirect('home')

@login_required
def delete_user(request,pk):
    """
    - Deletes a specific user from the database based on the provided primary key.
    - Displays a success message upon successful deletion.
    """
    user = CustomUser.objects.get(id=pk)
    user.delete()
    messages.success(request,'user Deleted')
    return redirect('home')

@login_required
def delete_announcement(request,pk):
    """
    - Deletes a specific event from the database based on the provided primary key.
    - Displays a success message upon successful deletion.
    - only admin can do this
    """
    Announcement = SpecialAnnouncement.objects.get(id=pk)
    Announcement.delete()
    messages.success(request,'Announcement Deleted')
    return redirect('home')

def About(request):
    """ 
    - Renders the 'about.html' template.
    - Simple view representing the about page.
    """
    return render(request,'about.html')

def logout(request):
    """ 
    - Logs the user out and redirects to the login page.
    - Displays a success message upon successful logout.
    """
    auth_logout(request)
    messages.success(request,'Logout successfully!!')
    return redirect('home')

@login_required
def AddEvents(request):
    """ 
    - Handles the addition of new events.
    - Renders the 'add_event.html' template.
    - Supports both GET and POST requests.
    - If POST request is valid, a new event is added, and success/error messages are displayed.
    """
    
    if request.method == 'POST':
        form = EventsForm(request.POST,request.FILES)
        if form.is_valid():
            event = form.save(commit = False)
            event.save()
            messages.success(request,'Event Added')
        else:
            messages.error(request,'Something wrong,try again..')
    else:
        form = EventsForm()
    context = {'forms':form}
    return render(request,'add_event.html',context)

@login_required
def Dashboard(request):
    """ 
    - Retrieves all users from the database.
    - Renders the 'index.html' template with the retrieved users.
    """
    users = CustomUser.objects.all()
    return render(request,'index.html',{'users':users})


def announcement_form(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        SpecialAnnouncement.objects.create(title=title, content=content)
        messages.success(request,'Announcement Added.')
        return redirect('home')
    return render(request, 'announcement_form.html')

