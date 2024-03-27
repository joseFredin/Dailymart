from django.urls import path
from . import views
urlpatterns = [
    path('' , views.index , name='index'),
    path('addcategories' , views.addcategories , name='addcategories'),
    path('addproducts' , views.addproducts , name='addproducts'),
    path('categories' , views.categories , name='categories'),
    path('products' , views.products ,name='products'),
    path('table' , views.table , name='table'),
    path('Edit/<int:id>' , views.Edit , name='Edit'),
    path('update/<int:id>' , views.update , name='update'),
    path('Delete/<int:id>' , views.Delete , name='Delete'),
    path('table1' , views.table1 , name='table1'),
    path('Edit1/<int:id>' , views.Edit1 , name='Edit1'),
    path('update1/<int:id>' , views.update1 , name='update1'),
    path('Delete1/<int:id>' , views.Delete1 , name='Delete1'),
    path('contacttable' , views.contacttable , name='contacttable'),
    path('registertable' , views.registertable , name='registertable'),
    path('ordertable' , views.ordertable , name='ordertable')
]
