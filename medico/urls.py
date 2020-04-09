"""medico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from home import views
from products.api import ProductView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.HomePage,name='home'),
    path('home',views.HomePage,name='home'),
    path('login',views.Login,name='login'),
    path('logout',views.Logout,name='logout'),
    path('register',views.Register,name='register'),
    path('medicine',views.allMedicine,name='medicine'),
    path('base',views.base,name='base'),
    path('cart',views.viewCart,name='cart'),
    path('s',views.SearchProduct,name='search'),
    path('about',views.About,name='about'),
    path('contact',views.Contact,name='contact'),
    path('checkout',views.Checkout,name='checkout'),
    path('thankyou',views.Thankyou,name='thankyou'),
    url(r'^productsapi/$',ProductView.as_view(), name='PView' ),
    url( r'^removeCart/(?P<slug>[\w-]+)',views.RemoveCart, name="RemoveCart"),
    url( r'^cart/(?P<slug>[\w-]+)',views.UpdateCart, name="updateCart"),
    url( r'^(?P<slug>[\w-]+)',views.MedDescription, name="MedDescription"),

]
