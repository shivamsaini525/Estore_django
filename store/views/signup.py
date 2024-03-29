from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..models.product import Product
from ..models.category import Category
from ..models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import sessions


def validateCustomer(customer):
   error_message=None

   if(not customer.first_name):
      error_message="First Name is Required"
   elif len(customer.first_name) < 3:
      error_message ="First Name must be 3 Char long or more"
   elif not customer.last_name:
      error_message="Last Name is Required"
   elif not customer.phone:
      error_message="Phone is Required"
   elif len(customer.phone) < 10:
      error_message="Phone Number is Incorrect"
   elif not customer.email:
      error_message="Email is Required"
   elif len(customer.password) < 6:
      error_message="Password must be 6 char long or more"
   elif  customer.isExit():
      error_message="Email Already used"   
   return error_message 

def registerUser(request):
      postdata=request.POST

      first_name=postdata.get('first_name')
      last_name=postdata.get('last_name')
      email=postdata.get('email')
      phone=postdata.get('phone')
      image=postdata.get('image')
      address=postdata.get('address')
      city=postdata.get('city')
      state=postdata.get('state')
      password=postdata.get('password')
      
      #old values for form
      value={
         'first_name' : first_name,
         'last_name': last_name,
         'email': email,
         'phone':phone,
         'image':image,
         'address':address,
         'city':city,
         'state':state,
      }

      customer=Customer(
         first_name=first_name,
         last_name=last_name,
         email=email,
         phone=phone,
         image=image,
         address=address,
         city=city,
         state=state,
         password=password
      )

      error_message=validateCustomer(customer)  

      if not error_message:
         customer.password=make_password(customer.password)
         customer.register()
         return redirect('home')
      else:
         data= {'error':error_message,
                'values': value}
         return render(request,'signup.html', data)


def signup(request):
   if request.method == "GET":
     return render(request,'signup.html')
   else:
     return registerUser(request)