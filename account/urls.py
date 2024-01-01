from django.urls import path
from .views import Signup,Login,Logout,VerifyUser,ResetpasswordView,Verifytoken,Changepassword

urlpatterns = [
    path('register/',Signup.as_view(),name='signup'),
    path('Login/',Login.as_view(),name='Login'),
    path('Logout/',Logout.as_view(),name='Logout'),
    path('verify/<id>/<token>/',VerifyUser.as_view(),name='activate'),
    path('reset/',ResetpasswordView.as_view(),name='reset'),
    path('confirmreset/<id>/',Verifytoken.as_view(),name='tokenverify'),
    path('changepassword/',Changepassword.as_view(),name='changepassword')
  
]