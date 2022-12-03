from django.shortcuts import render
# from django.contrib import messages

# Create your views here.

# db
from pymongo import MongoClient

from .models import Responseneed, details

client = MongoClient("mongodb://127.0.0.1:27017/")
db = client['Details']
coll = db.info


def sample(request):
    return render(request, 'my_app/index.html')


def signin(request):
    return render(request, 'my_app/login.html')


def signup(request):
    return render(request, 'my_app/signup.html')


def appres(request):  # appointment details
    if request.method == 'POST':
        name = request.POST.get('name')
        phn = request.POST.get('ph')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        db.coll.insert_one({'name': name, 'phn': phn, 'email': email, 'message': msg})
        c = Responseneed(name=name, msg=msg, email=email)  # admin table
        c.save()
        return render(request, 'my_app/res.html')
    else:
        pass


def getres(request):  # signup details
    # msg=None
    if request.method == 'POST':
        firstname = request.POST.get('f_name')
        lastname = request.POST.get('l_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        a = details(firstname=firstname, lastname=lastname, email=email, password=password)  # admin table
        a.save()
        db.coll.insert_one({'firstname': firstname, 'lastname': lastname, 'email': email, 'password': password})
        # messages.success(request,"successfully signed")
        return render(request, 'my_app/login.html')
    else:
        # messages.success(request,"password wrong")
        return render(request, 'my_app/signup.html')


def checkuser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        c = db.coll.find_one({'email': email})
        if c['email'] == email and c['password'] == password:
            return render(request, "my_app/index.html")
        else:
            return render(request, "my_app/login.html")
    else:
        pass
