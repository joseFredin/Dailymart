from django.shortcuts import render , redirect
from .models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from userapp.models import*

# Create your views here.
def index (request):
    categories = Categories.objects.all().count()
    products = Products.objects.all().count()
    users = Register.objects.all().count()
    cart = Cart.objects.all().count()
    return render (request , 'index.html' , {'categories' : categories , 'products' : products , 'users' : users , 'cart' : cart})
def addcategories (request):
    return render (request , 'add categories.html')
def addproducts (request):
    return render (request, 'add products.html')
def categories (request):
    if request.method == 'POST':
        name = request.POST['name']
        image = request.FILES['image']
        description = request.POST['description']
        data = Categories (Name = name , Image = image , Description = description)
        data.save()
    return redirect ('addcategories')
def products (request):
    if request.method == 'POST':
        name = request.POST['name']
        image = request.FILES['image']
        price = request.POST['price']
        quantity = request.POST['Quantity']
        category = request.POST['category']
        data = Products(Name = name , Image = image , Price = price , Quantity = quantity , Category = category)
        data.save()
    return redirect ('addproducts')
def table (request):
    data  = Categories.objects.all()
    return render (request , 'table.html' , {'data' : data})
def Edit (request,id):
    data  = Categories.objects.filter(id = id)
    return render (request , 'Edit.html' , {'data' : data})
def update (request , id):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        try:
            img_c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Categories.objects.get(id=id).Image
        Categories.objects.filter(id = id).update(Name = name , Image = file , 
                                                  Description = description)
        return redirect ('table')
def Delete (request , id):
    Categories.objects.filter(id = id).delete()
    return redirect ('table')
def table1 (request):
    data = Products.objects.all()
    return render (request , 'table1.html' , {'data' : data})
def Edit1 (request , id):
    data = Products.objects.filter(id = id)
    return render (request , 'Edit1.html' , {'data' : data})
def update1 (request , id):
     if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        quantity = request.POST['Quantity']
        category = request.POST['category']
        try:
            img_c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Products.objects.get(id=id).Image
        Products.objects.filter(id = id).update(Name = name , Image = file , Price = price , Quantity = quantity , Category = category)
        return redirect ('table1')
def Delete1 (request , id):
    Products.objects.filter(id = id).delete()
    return redirect ('table1')
def contacttable (request):
    data = Contact.objects.all()
    return render (request , 'contacttable.html' , {'data' : data})
def registertable (request):
    data = Register.objects.all()
    return render (request , 'registertable.html' , {'data' : data})
def ordertable (request):
    data = Cart.objects.all()
    return render (request, 'ordertable.html' , {'data' : data}) 
