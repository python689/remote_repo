from django.shortcuts import render, redirect
from loginapp.models import RegistationData,ProductData
from loginapp.forms import RegistrationForm, LoginForm,InsertingData,UpdateData,DeletingDataForm
from django.http.response import HttpResponse

def index(request):
    return render(request,'home.html')


def registrationview(request):
    if request.method=="POST":
        rform=RegistrationForm(request.POST)
        if rform.is_valid():
            fname=request.POST.get('firstname')
            lname=request.POST.get('lastname')
            uname=request.POST.get('username')
            pwd=request.POST.get('password')
            mobile=request.POST.get('mobile')
            email=request.POST.get('email')
            gender=rform.cleaned_data.get('gender')
            dob=rform.cleaned_data.get('date_of_birth')

            data=RegistationData(
                firstname=fname,
                lastname=lname,
                username=uname,
                password=pwd,
                mobile=mobile,
                email=email,
                gender=gender,
                date_of_birth=dob
            )
            data.save()
            rform=RegistrationForm()
            return render(request,'registration.html',{'rform':rform})
        else:
            return HttpResponse("Invalid Input")

    else:
        rform=RegistrationForm()
        return render(request,'registration.html',{'rform':rform})


def loginview(request):
    if request.method=="POST":
        lform=LoginForm(request.POST)
        if lform.is_valid():
            uname = request.POST.get('username')
            pwd = request.POST.get('password')
            uname1=RegistationData.objects.filter(username=uname)
            pwd1=RegistationData.objects.filter(password=pwd)
            if uname1 and pwd1:
                return redirect("/index/")
            else:
                return HttpResponse("Login Failed")


        else:
            return HttpResponse("Invalid User")
    else:
        lform=LoginForm()
        return render(request,'login.html',{'lform':lform})


def home(request):
    return render(request,'home.html')


def createview(request):
    if request.method=="POST":
            product_id=request.POST.get('product_id')
            product_name=request.POST.get('product_name')
            product_cost=request.POST.get('product_cost')
            product_class=request.POST.get('product_class')
            no_of_products=request.POST.get('no_of_products')
            customer_name = request.POST.get('customer_name')
            mobile = request.POST.get('mobile')
            email = request.POST.get('email')
            manufacture_date=request.POST.get('manufacture_date')
            expiry_date=request.POST.get('expiry_date')

            data=ProductData(
                product_id=product_id,
                product_name=product_name,
                product_cost=product_cost,
                product_class=product_class,
                no_of_products=no_of_products,
                customer_name=customer_name,
                mobile=mobile,
                email=email,
                manufacture_date=manufacture_date,
                expiry_date=expiry_date
            )
            data.save()
            return render(request, 'create.html')

    else:
        return render(request,'create.html')


def retriveview(request):
    data=ProductData.objects.all()
    return render(request,'retrive.html',{'pdata':data})


def updateview(request):
    if request.method=="POST":
            product_id=request.POST.get("product_id")
            product_cost=request.POST.get("product_cost")
            pro_id=ProductData.objects.filter(product_id=product_id)
            if not pro_id:
                return HttpResponse("Product is not availabel")
            else:
                pro_id.update(product_cost=product_cost)
                return render(request,'update.html')
    else:
        return render(request, 'update.html')


def deleteview(request):
    if request.method=="POST":
        product_id=request.POST.get("product_id")
        pro_id=ProductData.objects.filter(product_id=product_id)
        if not pro_id:
            return HttpResponse("Product is not availabel")
        else:
            pro_id.delete()
            return render(request,'delete.html')
    else:
        return render(request,'delete.html')