from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Person, TimeTable, Subject
# from app01.forms import Image
from .form import SignUpForm, Icon, TimeTableForm
# Create your views here.
def home(request):
    return render(request, 'authtest/home.html')

@login_required
def private_page(request):
    if request.method == "POST":
        form = Icon(request.POST, request.FILES)
        p = request.user.userinfo
        if form.is_valid():
            p.icon=request.FILES.get('icon')
        else:
            p.icon=False
        p.age = request.POST["age"]
        p.username = request.POST["username"]
        p.save()
        
        #ここから時間割
        
    else:
        form = Icon()
        timetableform = TimeTableForm(instance=request.user.userinfo.timetable)
    timetableform = TimeTableForm(instance=request.user.userinfo.timetable)
    return render(request, 'authtest/private.html', {'form': form, 'timetableform': timetableform})

def public_page(request):
    return render(request, 'authtest/public.html', {})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            userform = form.save(commit=False)
            person = Person(user=userform)
            userform.save()
            person.save()
            return redirect('login')

    else:
        form = SignUpForm()
    return render(request, 'authtest/signup.html', {'form': form})

def top_page(request):
    return render(request, 'app01/top.html', {})

def start_page(request):
    return render(request, 'authtest/start.html', {})

def mypage(request):
    return render(request, 'authtest/mypage.html', {})