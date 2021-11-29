from django.urls import path
from . import views
#URLconfig
from .views import (
    dynamic_view,
    render_initial_data,
    delete,
    list_view,
    product_create,
    # CustomerFormView,
    CustomerCreate,
    home,
    Search,
    Search_Product,
    customer_view,
    customer_delete,
customer_list,
)
app_name = 'website'
urlpatterns = [
    path('product/<int:my_id>/', dynamic_view, name='product-detail'),
    path('product/<int:my_id>/delete', views.delete, name = 'delete-product'),
    path('product/list/',list_view,name='list'),
    #path('product/',views.product_details,name ='product-details'),# not calling function, just passing referance
    path('product/create/',product_create),
    path('customer/add/',CustomerCreate,name = "Customer"),
    path('customer/detail/<int:customer_id>/', customer_view, name = 'customer-detail'),
    path('customer/delete/<int:customer_id>/', customer_delete, name = 'customer-delete'),
    path('',home, name='home'),
    path('customer/search',Search),
    path('product/search',Search_Product),
    path('customer/list',customer_list)

]
