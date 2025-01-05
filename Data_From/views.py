from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        user = User(name=name,email=email,phone=phone,password=password)
        user.save()
        return HttpResponse('Data Saved Successfully')
    return render(request,'Data_From/login.html')

def product_list(request):
    # Fetch all products
    datas = User.objects.all()
    print(datas)
    return render(request, 'Data_from/datafetch.html', {'datas': datas})