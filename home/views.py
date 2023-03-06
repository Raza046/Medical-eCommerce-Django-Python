from django.shortcuts import render, HttpResponseRedirect, Http404,redirect
from django.shortcuts import get_list_or_404, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.forms.models import modelformset_factory
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from products.models import Products
from carts.forms import CartItemsForm
from orders.models import Order
from orders.forms import OrderForm
from carts.models import myCart, CartItems

# Create your views here.


def HomePage(request):

    context = locals()

    template = 'home.html'
    return render(request,template,context)


def allMedicine(request):

    context ={ "prod" :  Products.objects.all()}

    template = 'medicines.html'
    return render(request,template,context)


def SearchProduct(request):

    try:
        s = request.GET.get('s') 
    except:
        s = None
    if s:
        products = Products.objects.get(name__icontains = s )
        cart_items, created = CartItems.objects.get_or_create(prod=products,user=request.user)
        
        formset = CartItemsForm(request.POST , instance=products)
        
        if formset.is_valid():
            formset.save()

        context = {'query': s , 'prod':products , "form":formset}
        template = 'descriptions.html'

    else:
        template = 'medicines.html'
        context = {}

    return render(request,template,context)



def MedDescription(request,slug):

    prod = Products.objects.get(slug=slug)
    cart_items, created = CartItems.objects.get_or_create(prod=prod,user=request.user)
#    NewComment, commentCreated = UserComments.objects.get_or_create(user=request.user)
        
    formset = CartItemsForm(request.POST , instance=cart_items)
 #   CommentFormset = CommentForm(request.POST , instance=NewComment)
        
    if formset.is_valid():
        formset.save()
  #      CommentFormset.save()

    context ={ "prod":prod , "form":formset }

    template = 'descriptions.html'

    return render(request,template,context)


def viewCart(request):

    try:
        cart1 = myCart.objects.get(user=request.user)
        cart = myCart.objects.filter(user=request.user).first()
     
        totals = 0.00
        all_total = 0

        for items1 in cart.items.all():

            totals = float(items1.prod.price * items1.quantity)
            items1.total = totals
            all_total += totals
            items1.save()
 
        cart.subtotal=all_total
        cart.save()
        
        context = {"carts": cart}

        template = 'cart.html'

        return render(request,template,context)

    except myCart.DoesNotExist:

        carts = myCart.objects.create(user=request.user)

        context=locals()

        template = 'cart.html'
        return render(request,template,context)


def UpdateCart(request,slug):

    try:

        cart= myCart.objects.get(user=request.user)

        prods = Products.objects.get(slug=slug)
        if Products.DoesNotExist:
            pass
        
        cart_items, created = CartItems.objects.get_or_create(prod=prods,user=request.user)
        
        if cart_items in cart.items.all():
            pass
           
        if not cart_items in cart.items.all():
            
            cart.items.add(cart_items)

        totals = 0.00
        all_total = 0

        for items1 in cart.items.all():

            totals = float(items1.prod.price * items1.quantity)
            items1.total = totals
            all_total += totals
            items1.save()
 
        cart.subtotal=all_total
        cart.save()
        
        return HttpResponseRedirect(reverse("cart"))

    except myCart.DoesNotExist:

        cart = myCart.objects.create(user=request.user)
        cart.save()

        cart1= get_object_or_404(myCart,user=request.user)

        try:
            prods = Products.objects.get(slug=slug)
        except Products.DoesNotExist:
            pass
        except:
            pass

        cart_items, created = CartItems.objects.get_or_create(prod=prods,user=request.user)

        if not cart_items in cart.items.all():
            cart.items.add(cart_items)

        totals = 0.00
        new_totals = 0.00
                
        for items1 in cart.items.all():

            totals = float(items1.prod.price) * items1.quantity
            new_totals += totals

        cart.total=totals
        cart.subtotal=new_totals

        cart.save()

        return HttpResponseRedirect(reverse("cart"))


def About(request):

    context = locals()
    template = "about.html"

    return render(request,template,context)


def Contact(request):

    context = locals()
    template = "contact.html"

    return render(request,template,context)

def Thankyou(request):

    context = locals()
    template = "thankyou.html"

    return render(request,template,context)

def Checkout(request):


    try:
        carts = myCart.objects.get(user=request.user)
        order1 = Order.objects.get(user=request.user)
        orders = Order.objects.filter(user=request.user).first()  
        form = OrderForm(request.POST,instance=order1)
        
        if form.is_valid():

            cart = myCart.objects.get(user=request.user)
            form.instance.cart=cart
            form.save()
            

        context = {'form':form , 'cart' : carts, 'orders':orders}
        template = "order.html"

        return render(request,template,context)


    except Order.DoesNotExist:
            
        order = Order.objects.create(user=request.user)
        cart= get_object_or_404(myCart,user=request.user)

        order1 = Order.objects.get(user=request.user)
        form = OrderForm(request.POST,instance=order1)

        if form.is_valid():
            form.save()


        context = {'cart' : cart , 'form':form} 

        template = "order.html"
        return render(request,template,context)


    return render(request,template,context)


def RemoveCart(request,slug):

    carts = myCart.objects.filter(user=request.user).first()
    prods = Products.objects.get(slug=slug)
    cart_items, created = CartItems.objects.get_or_create(prod=prods,user=request.user)
    
    try:

        if cart_items in carts.items.all():

            carts.items.remove(cart_items)
            carts.save()

            return redirect("/cart")

        else:

            return redirect("/cart")

    except myCart.DoesNotExist:

        carts = myCart.objects.create(user=request.user)

        context = locals()
        template = 'cart.html'
        return render(request,template,context)

    return HttpResponseRedirect(reverse("cart"))


def base(request):

    template = 'base.html'
    return render(request,template)


def Login(request):

    if request.method == "POST":

        username = request.POST['username']
        psw = request.POST['psw']
        
        user = auth.authenticate(username=username,password=psw)

        if user is not None:

            auth.login(request,user)
            return redirect("/home")

        else:
            messages.info(request,"Usernname or Password Incorrect")
            return redirect("/login")

    else:
          
        template = 'login.html'
        return render(request,template)


def Register(request):


    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        psw = request.POST['psw']
        psw2 =  request.POST['psw2']
        contact =  request.POST['contact']

        if psw == psw2:

            if User.objects.filter(username=username).exists():
                messages.info(request,"Usernname already Taken")
                return redirect("/register")

            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already Taken")
                return redirect("/register")

            user1=User.objects.create_user(username=username,email=email,password=psw)
            user1.save()
            return redirect("/login")

        else:

            messages.info(request,"Password not Same")
            return redirect("/register")

    else:
        template = "register.html" 
        return render(request,template)


def Logout(request):

    auth.logout(request)
    return redirect("/login")
