from django.urls import path, include
from .views import Article_details,delete


urlpatterns = [
    path('details/',Article_details,name = 'details'),
    path('<int:my_id>/delete', delete, name='delete')

]


