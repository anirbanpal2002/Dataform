from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User

# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            user = User(name=name,email=email,phone=phone,password=password)
            user.save()
            return redirect('cong')
        else:
            return HttpResponse('Password not matched')
    return render(request,'Data_From/login.html')


def sign(request):
    if request.method == 'POST':
        email = request.POST['email']
        pass1= request.POST['password']
        user=authentication(email,pass1)
        if user:
            return redirect('cong')
        else:
            return HttpResponse('Invalid credentials')
    
        
    return render(request,'Data_From/sign.html')



def authentication(email,pass1):
    try:
        user = User.objects.get(email=email,password=pass1)
        return user
    except User.DoesNotExist:  
        return None
    
def index(request):
    return render(request,'Data_From/home.html')

def cong(request):
    return render(request,'Data_From/cong.html')

# def product_list(request):
#     # Fetch all products
#     datas = User.objects.all()
#     print(datas)
#     return render(request, 'Data_from/datafetch.html', {'datas': datas})


