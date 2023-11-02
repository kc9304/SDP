from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from .models import Login, Signup1, Comic, Personal


# Create your views here.
def base(request):
    return render(request, 'loginpage/base.html')
def contact(request):
    return render(request, 'loginpage/contact.html')

def cart(request):
    return render(request, 'loginpage/cart.html')

def register(request):
    return render(request, 'loginpage/regiister.html')


def addregister(request):
    if request.method == 'POST':
        name = request.POST['name']
        psw = request.POST['psw']
        new_id = Signup1(name=name, psw=psw)
        new_id.save()
        return render(request,"loginpage/home.html")

    else:
        return render(request,"loginpage/error.html");





def addpersonal(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']
        alternate_phone = request.POST['alternate_phone']
        landmark = request.POST['landmark']
        pincode = request.POST['pincode']
        city = request.POST['city']
        town = request.POST['town']

        personal = Personal(  first_name=first_name,middle_name=middle_name,last_name=last_name, address=address,landmark=landmark,pincode=pincode,city=city,town=town, email=email,phone_number=phone, alternative_number=alternate_phone)
        personal.save()
        return render(request, "bookspage/success.html")  # Create a success.html template or use any other page for success.



def login(request):
        return render(request, 'loginpage/login.html')


def home(request):
    return render(request, 'loginpage/home.html')


def home2(request):
    return render(request, 'loginpage/home2.html')


def checklogin(request):
    uname = request.POST["uname"]
    pwd = request.POST["pwd"]
    flag = Signup1.objects.filter(Q(name=uname) & Q(psw=pwd))
    context = {
        'uname':uname,
    }
    request.session['uname'] = uname
    print(flag)
    if flag and uname=="kc":
        return render(request,"bookspage/kc.html",context)
    if flag:
        return render(request, "loginpage/home2.html",context)
    else:
        return render(request, "loginpage/error.html")


def checkbook(request):
    name = request.GET["name"]
    flag = Comic.objects.filter(Q(name=name))
    print(flag)

    if flag:
        if name == "comic":
            return render(request, "bookspage/comic.html")
        elif name == "adventure":
            return render(request, "bookspage/adventure.html")
        elif name == 'demon slayer vol1':
            return render(request, 'bookspage/vol1.html')
        elif name == 'demon slayer vol2':
            return render(request, 'bookspage/vol2.html')
        elif name == 'demon slayer vol3':
            return render(request, 'bookspage/vol3.html')
        elif name == 'demon slayer vol4':
            return render(request, 'bookspage/vol4.html')
        elif name == 'demon slayer vol5':
            return render(request, 'bookspage/vol5.html')
        elif name == 'demon slayer vol6':
            return render(request, 'bookspage/vol6.html')
        elif name == 'demon slayer vol7':
            return render(request, 'bookspage/vol7.html')
        elif name == 'demon slayer vol8':
            return render(request, 'bookspage/vol8.html')
        elif name == 'demon slayer vol9':
            return render(request, 'bookspage/vol9.html')
        elif name == 'demon slayer vol10':
            return render(request, 'bookspage/vol10.html')

    else:
        return render(request, "loginpage/error.html")
  # Adjust the import based on your actual model

def profile(request):
    uname = request.session.get('uname')

    context = {
        'uname': uname,
    }

    return render(request, 'loginpage/profile.html', context)


def form(request):
    return render(request, 'loginpage/buyform.html')

def vieworder(request):
    personal = Personal.objects.all()

    return render(request, 'loginpage/vieworder.html',{"personal": personal})