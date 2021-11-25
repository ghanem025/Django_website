from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404,Http404,redirect
from .models import Product,Customer
from .forms import ProductForm, RawForm,CustomerForm,SearchForm
from django.views.generic import FormView, TemplateView, ListView
from django.db.models import Q




def home(request):
    template = "home.html"
    context = {}
    return render(request,"home.html",context)


def list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list':queryset
    }
    return render (request, "product/list.html", context)


def delete(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    else:
        print("we did not delete it ")
    context = {
        'object': obj
    }
    return render(request, "product/delete.html", context)

def customer_view(request, customer_id):
    obj = get_object_or_404(Customer,id=customer_id)
    return render(request,"customer/detail.html",{'object':obj})
def dynamic_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    context = {
        'object':obj
    }
    return render(request, "product/detail.html", context)


def render_initial_data(request):
  #this function lets you render data from the start of the form
  #it also lets you change the value of models using forms
    initial_data = {
        'title': "My this awesome title"
    }
    obj = Product.objects.get(id=1)#grab an object
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        print('this form is valid')
        form.save()
    else:
        print('not valid')
    context = {
        'form': form
    }
    return render(request, "product/product_create.html", context)



def CustomerCreate(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CustomerForm()
    context = {
        'form':form
    }
    return render(request,"customer/AddCustomer.html",context)


def product_create(request):
    form = ProductForm(request.POST or None)# renders the form
    if form.is_valid():#if the form is valid than save it to the database
       form.save()
       form = ProductForm() #rerender the form
    context = {
       'form': form
    }
    return render(request, "product/product_create.html", context)


def product_details(request):
    obj = Product.objects.get(id=1)
    context = {
        'object' : obj# this 'object' is taken from website.models
    }
    return render(request, "product/detail.html", context)


def Search(request):
    templatename = "customer/Search.html"
    if 'q' in request.GET: #
        q = request.GET['q']
        object_list = Customer.objects.filter(first_name__startswith=q)# filter through the objects and see if a name matches 'q'
        if (len(object_list))<=0:
            return render(request, "customer/NotFound.html",{} )# render the site
    else:
        object_list = Customer.objects.all()#show all the customers in the database if you searched nothing

    context = {
        'object': object_list
    }
    return render(request, templatename,context)# render the site


def Search_Product(request):
    template = "product/Search.html"
    if 'q' in request.GET: #
        q = request.GET['q']
        object_list = Product.objects.filter(title__startswith=q)# filter through the objects and see if a name matches 'q'
        if(len(object_list)<=0):
            return render(request,"product/NotFound.html",{})
    else:
        object_list = Product.objects.all()#show all the products in the database if you searched nothing
    context = {
        'products': object_list
    }
    return render(request, template,context)# render the site
