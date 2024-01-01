from django.shortcuts import render,redirect
from django.views import View
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from django.utils.encoding import smart_str,force_bytes,DjangoUnicodeDecodeError
from .authentication_backends import CustomAuthBackend

from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode

from django.contrib.auth.tokens import PasswordResetTokenGenerator

def send_mail_verify(email ,token):
           subject = 'Your account to be verified'
           message =token
           email_from = settings.EMAIL_HOST_USER
           recipient_list = [email,'aaryanshah615@gmail.com']
           send_mail(subject, message , email_from ,recipient_list)

class Signup(View): 
        def get(self, request, *args, **kwargs):
            return render(request,'signup.html')  

        def post(self, request, *args, **kwargs):       
            fname = request.POST['fname']
            lname = request.POST['lname']
            phone = request.POST['number']
            email = request.POST['email']
            password = request.POST['password']
            print(password)

            if User.objects.filter(email=email):
               messages.error(request, "username already exits please try some others")
               print('hello')
               return redirect('signup')
            else:
                my_user=User.objects.create_user(email=email,name=fname + lname,ph=phone)
                my_user.set_password(password)
                my_user.save()           
                uid=urlsafe_base64_encode(force_bytes(my_user.id))
                token=PasswordResetTokenGenerator().make_token(my_user)
                link='http://127.0.0.1:8000/verify/'+uid+'/'+token
                send_mail_verify(email,link)
                messages.success(request,"Please Verify your Account")
                return redirect('Login')
                         

class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request,'login.html') 
    def post(self, request, *args, **kwargs): 
             email = request.POST['email']
             password = request.POST['password']
             user=User.objects.get(email=email)
             if user.is_active:
              myuser = authenticate(email=email,password=password)
              if myuser is not None:
                login(request,myuser)
                request.session['email'] =email
                request.session['n'] =0
                messages.success(request,"Login successfully")
                return redirect('home')
              else:
               messages.warning(request,"Password or Username donot match") 
             else:
                messages.success(request,"Please Verify your account")
                return redirect('Login')
                   
       

class Logout(View):
   def get(self, request, *args, **kwargs):
     logout(request)
     return redirect('Login')
   
'''
class Verify(View):
    def get(self, request,uid,token, *args, **kwargs):
        id = smart_str(urlsafe_base64_decode(uid))
        user=User.objects.get(id=id)
        if not PasswordResetTokenGenerator().check_token(user,token):
            messages.warning(request,"Token expired") 
            return redirect('Login')
        else:
            user.tc=True
            user.save()
            messages.success(request,"your email Verified")
            return redirect('Login')
'''