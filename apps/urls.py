from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(),name='home'),
    path('account/',Account.as_view(),name='account'),
    path('contact/',contact.as_view(),name='contact'),
    path('cart/',Cartview.as_view(),name='cart'),
    path('cartdel/<id>',Cartdel.as_view(),name='cartdel'),
    path('orderbook/',OrderBook.as_view(),name='order'),
    path('order/',OrderView.as_view(),name='orderview'),
    path('documents/<int:document_id>/', BookDoc_View.as_view(), name='open_document'),
   
]