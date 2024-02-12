from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..models.product import Product
from ..models.category import Category
from ..models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import sessions

def login(request):
   if request.method == "GET":
      return render(request, 'login.html')   
   else:
      postdata=request.POST
      email=postdata.get('email')
      password=postdata.get('password')
      customer=Customer.get_customer_by_email(email)

      error_message=None
      if customer:
            flag=check_password(password ,customer.password)
            if flag:
               request.session['customer_id']=customer.id
               request.session['email']=customer.email
               return redirect('home')
            else:
               error_message="Passwod is Wrong"
               return render(request,'login.html',{'error':error_message})
               
      else:
         error_message="Email or Password is Wrong"
         return render(request,'login.html',{'error':error_message})

