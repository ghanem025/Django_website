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
    CustomerCreate
)
app_name = 'website'
urlpatterns = [
    path('product/<int:my_id>/', dynamic_view, name='product-detail'),
    path('product/<int:my_id>/delete', views.delete),
    path('product/list/',list_view,name='list'),
    #path('product/',views.product_details,name ='product-details'),# not calling function, just passing referance
    path('product/create/',product_create),
    path('customer/add/',CustomerCreate,name = "Customer")
]
