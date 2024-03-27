from django.shortcuts import render ,redirect
from Adminapp.models import*
from .models import*
from django.db.models.aggregates import Sum

# Create your views here.
def user (request):
    data = Categories.objects.all()
    return render (request , 'user.html' , {'data' : data})

def contact (request):
    a = request.session.get('u_id')
    count = Cart.objects.filter(userid = a , status = 0).count
    return render (request , 'contact.html' , {'count' : count})

def tocontact (request):
    if request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['mail']
        number = request.POST['number']
        message = request.POST['Message']
        data = Contact (Name = name , Mail = mail , Number = number , Message = message)
        data.save()
    return redirect ('contact')

def register (request):
    return render (request , 'register.html')

def toregister (request):
    if request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['mail']
        number = request.POST['number']
        password = request.POST['password']
        data = Register(Username = name , Mail = mail , Number = number , Password = password)
        data.save()
    return redirect ('register')

def login (request):
    return render (request , 'login.html')

def publicdata(request):
    if request.method == "POST":
        username=request.POST.get('name')
        password=request.POST.get('password')
        if Register.objects.filter(Username=username,Password=password).exists():
            data = Register.objects.filter(Username=username,Password=password).values('id','Number','Mail').first()
            request.session['u_id'] = data['id']
            request.session['phonenumber_u'] = data['Number'] 
            request.session['email_u'] = data['Mail'] 
            request.session['username_u'] = username
            request.session['password_u'] = password
            return redirect('userlogin') 
        else:
            return render(request,'login.html',{'msg':'invalid user credentials'})
    else:
        return redirect('login')
    
def userlogout(request):
    del request.session['u_id']
    del request.session['phonenumber_u']
    del request.session['email_u']
    del request.session['username_u']
    del request.session['password_u']
    return redirect('login')

def userlogin (request):
    a = request.session.get('u_id')
    count = Cart.objects.filter(userid = a , status = 0).count
    data = Categories.objects.all()
    data1 = Products.objects.all()
    return render (request , 'userlogin.html' , {'data' : data , 'data1' : data1 , 'count' : count})

def viewproduct (request , id):
    a = request.session.get('u_id')
    count = Cart.objects.filter(userid = a , status = 0).count
    data = Products.objects.filter(id = id)
    return render (request , 'viewproduct.html' , {'data' : data , 'count' : count})

def cart (request):
    a = request.session.get('u_id')
    count = Cart.objects.filter(userid = a ,status = 0).count()
    data = Cart.objects.filter(userid = a , status = 0)
    s = Cart.objects.filter(userid = a , status = 0).aggregate(Sum('total'))
    return render (request , 'cart.html' , {'data' : data , 's' : s , 'count' : count})

def checkout (request):
    a = request.session.get('u_id')
    s = Cart.objects.filter(userid = a ,status = 0).aggregate(Sum('total'))
    data = Cart.objects.filter(userid = a , status = 0)
    return render (request , 'checkout.html' , {'data' : data , 's' : s})

def cartdata (request,id):
    if request.method == "POST":
        user_id = request.session.get('u_id')
        quantity = request.POST['quantity']
        total = request.POST['total']
        data = Cart(userid = Register.objects.get(id=user_id) , productid = Products.objects.get(id=id), 
                    quantity = quantity , total= total)
        data.save()
    return redirect('cart')

def cartdelete (request , id):
    Cart.objects.filter(id = id).delete()
    return redirect ('cart')

def checkoutdata (request):
    if request.method == 'POST':
        userid = request.session.get('u_id')
        country = request.POST['country']
        state = request.POST['state']
        address = request.POST['address']
        city = request.POST['city']
        postcode = request.POST['postcode']
        order = Cart.objects.filter(userid = userid , status = 0)

        for i in order:
            data = Checkout(userid = Register.objects.get(id=userid) , cartid = Cart.objects.get(id=i.id) , Country = country,
                            State=state,Address=address,City=city,Postcode=postcode)
            data.save()
            Cart.objects.filter(id = i.id).update(status = 1)
    return redirect('lastpage')

def lastpage (request):
    return render (request , 'Lastpage.html')

def product (request,Category):
    a = request.session.get('u_id')
    count = Cart.objects.filter(userid = a , status = 0).count
    if(Category == "all"):
        data1 = Products.objects.all()
    else:
        data1 = Products.objects.filter(Category = Category)
    data2 = Categories.objects.all()
    return render (request , 'product.html' ,{'data1' : data1 , 'data2' : data2 , 'count' : count})

def about (request):
    a = request.session.get('u_id')
    count = Cart.objects.filter(userid = a , status = 0).count
    return render (request, 'about.html' ,{'count' : count})
