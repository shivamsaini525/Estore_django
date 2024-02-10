from django.http import HttpResponse
from django.shortcuts import render
from .models.product import Product
from .models.category import Category
from .models.customer import Customer


# Create your views here.
def index(request):
   products= None
   categories=Category.get_all_categories()
   categoryID=request.GET.get('category')
   if categoryID:
      products=Product.get_all_product_by_id(categoryID)
   else:
      products=Product.get_all_product()
   data={}
   data['products']=products
   data['categories']=categories

   return render(request,'index.html',data)


def signup(request):
   if request.method == "GET":
     return render(request,'signup.html')
   else:
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
      customer.register()
      return HttpResponse("signup success")