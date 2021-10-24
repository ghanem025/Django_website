from django.shortcuts import render, get_object_or_404,Http404,redirect
from .models import Product
from .forms import ProductForm, RawForm,CustomerForm
from django.views.generic import FormView


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

# Create your views here.
# def product_create(request):
#   this is a raw django form, this lets us enter data and verify if it corresponds with the form
#   if it's valid then we create a new object and added it to the database
#   otherwise we print out an error
#     form = RawForm(request.POST or None)#request.POST lets us actually get the data from the form
#     if form.is_valid():
#         print(form.cleaned_data)
#         Product.objects.create(**form.cleaned_data)
#     else:
#         print(form.errors)#print out error
#
#     context = {
#         'form': form
#     }
#     return render(request, "product/product_create.html", context)




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
