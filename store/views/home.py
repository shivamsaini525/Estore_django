from django.shortcuts import render, redirect
from ..models.product import Product
from ..models.category import Category
from django.contrib import sessions
from django.views import View

class Index(View):
   
   def post(self, request):
       product=request.POST.get('product')
       
       return redirect('home')

  



   def get(self,request):
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
        print(request.session.get('email'))
        print(request.session.get('customer_id'))

        return render(request,'index.html',data)
      


   
