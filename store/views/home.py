from django.shortcuts import render, redirect
from ..models.product import Product
from ..models.category import Category
from django.contrib import sessions
from django.views import View

class Index(View):
   
   def post(self, request):
        product=request.POST.get('product')
        cart=request.session.get('cart')
        if cart:
           quantity=cart.get(product)
           if quantity:
              cart[product]=quantity+1
           else:
               cart[product]=1
        else:
           cart={}
           cart[product]=1
        request.session['cart']=cart
        print('cart',request.session['cart'])
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
      #   print(request.session.get('email'))
       

        return render(request,'index.html',data)
      


   
