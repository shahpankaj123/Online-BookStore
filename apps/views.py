from django.shortcuts import render,redirect
from django.contrib import messages
from django.views import View
from .models import Product,Contact,Cart,CartItem,Order,OrderItem
from account.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

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
    

@method_decorator(login_required(login_url='Login'), name='dispatch')
class Cartview(View):
    def get(self,request):
        email = request.session.get('email')
        user = User.objects.get(email=email)
        cart_item = CartItem.objects.filter(cart__user=user)
        t=0
        for j in cart_item:
            t=t+j.quantity*j.product.price
            print(t)      
        msg='If you Ordered more than RS.5000 Get 25 Per Off'    
        return render(request, 'cart.html',{'cart':cart_item,'email':email,'totalprice':t,'msg':msg})


    
@method_decorator(login_required(login_url='Login'), name='dispatch')   
class Cartdel(View):    
    def get(self,request,id):
        card=CartItem.objects.get(id=id)
        card.delete()
        return redirect('cart')

@method_decorator(login_required(login_url='Login'), name='dispatch')
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
    
@method_decorator(login_required(login_url='Login'), name='dispatch')  
class OrderBook(View):
    def get(self,request):
        email = request.session.get('email')
        return render(request, 'checkout.html', {'email': email})
    
    def post(self,request):
        email = request.session.get('email')
        user = User.objects.get(email=email)
        OrderItem1=OrderItem.objects.filter(order__user=user)
        price=0
        for x in OrderItem1:
            price+=x.item_price*x.quantity
        order = Order.objects.create(user=user, total_price=0.0)
        cart_item = CartItem.objects.filter(cart__user=user)
        for d in cart_item:
            product1 = Product.objects.get(id=d.product.id) 
            order_item1 = OrderItem.objects.create(order=order, product=product1,quantity=d.quantity, item_price=product1.price)
        if price>5000:    
           order1= sum(item.item_price * item.quantity for item in order.orderitem_set.all())
           rs=order1-25*order1/100
           order.total_price=rs         
           msg='Contragulation You got 25 percentage off'
        else:
            order.total_price = sum(item.item_price * item.quantity for item in order.orderitem_set.all())   
            msg=''
        order.save() 
        messages.success(request, 'Your Order submitted successfully')   
        return render(request, 'checkout.html', {'email': email,'msg':msg})


@method_decorator(login_required(login_url='Login'), name='dispatch')
class OrderView(View):
    def get(self,request):
        email = request.session.get('email')
        user = User.objects.get(email=email)
        OrderItem1=OrderItem.objects.filter(order__user=user)
        return render(request, 'order.html', {'email': email,'data':OrderItem1})




 


