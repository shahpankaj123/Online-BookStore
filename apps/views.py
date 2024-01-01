from django.shortcuts import render,redirect
from django.contrib import messages
from django.views import View
from .models import Product,Contact,Cart,CartItem
from account.models import User
# Create your views here.
class Home(View):
    def get(self,request):
        product = Product.get_all_product()#[:540:10]
        email = request.session.get('email')
        cart_item_count=0
        if email:
          user = User.objects.get(email=email)
          cart_item_count = CartItem.objects.filter(cart__user=user).count()
        return render(request, 'index.html',{'products':product,'email':email,'n':cart_item_count})
    
    def post(self,request):
        proid = request.POST.get('proid')
        book = Product.objects.get( pk=proid)
        cart, created  = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=book)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        messages.success(request, 'Cart added successfully')   
        return redirect('home')    

class Cartview(View):
    def get(self,request):
        email = request.session.get('email')
        user = User.objects.get(email=email)
        cart_item = CartItem.objects.filter(cart__user=user)
        t=0
        for j in cart_item:
            t=t+j.quantity*j.product.price
            print(t)  
        return render(request, 'cart.html',{'cart':cart_item,'email':email,'totalprice':t})
    
class Cartdel(View):    
    def get(self,request,id):
        card=CartItem.objects.get(id=id)
        card.delete()
        return redirect('cart')


class Account(View):
    def get(self,request):
      email = request.user.email
      name = request.user.name
      ph= request.user.ph
      return render(request, 'account.html', {'email':email, 'name':name,'ph':ph})
    
class contact(View):
    def get(self,request):
        email = request.session.get('email')
        return render(request, 'contact.html', {'email': email})

    def post(self,request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        textarea = request.POST.get('textarea')
        data = Contact.objects.create(name=name, email=email, mobile=mobile, textarea=textarea)
        messages.success(request, 'your form submitted success fully')
        return redirect('home')  
    
