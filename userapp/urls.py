from django.urls import path 
from . import views

urlpatterns = [
    path('user' , views.user , name='user'),
    path('contact' , views.contact , name='contact'),
    path('tocontact' , views.tocontact , name='tocontact'),
    path('register' , views.register , name='register'),
    path('toregister' , views.toregister , name='toregister'),
    path('login' , views.login , name='login'),
    path('publicdata' , views.publicdata , name='publicdata'),
    path('userlogout' , views.userlogout , name='userlogout'),
    path('userlogin' , views.userlogin , name='userlogin'),
    path('viewproduct/<int:id>/' , views.viewproduct , name='viewproduct'),
    path('cart' , views.cart , name='cart'),
    path('checkout' , views.checkout , name='checkout'),
    path('cartdata/<int:id>/' , views.cartdata , name='cartdata'),
    path('cartdelete/<int:id>/' , views.cartdelete , name='cartdelete'),
    path('checkoutdata' , views.checkoutdata , name='checkoutdata'),
    path('lastpage' , views.lastpage , name='lastpage'),
    path('product/<str:Category>/' , views.product , name='product'),
    path('about' , views.about , name="about")
]