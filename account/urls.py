from django.urls import path
from .views import Signup,Login,Logout

urlpatterns = [
    path('register/',Signup.as_view(),name='signup'),
    path('Login/',Login.as_view(),name='Login'),
    path('Logout/',Logout.as_view(),name='Logout')
  
]