from django.urls import path
from . import views
#URLconfig
urlpatterns = [
    path('',views.hello),# not calling function, just passing referance
    path('front/',views.home),
    path('profile/',views.profile),
    path('navbar/',views.panel)

]