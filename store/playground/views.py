from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#view function are functions that take a request and a response (request handler) or action
#
def calc():
    x=3
    y=2
    return x
def hello(request):
    #pull data
    #send emails
    #return HttpResponse('hello world')
    x=calc()
    return render(request,'main.html',{'name': 'G'})

def home(request):
    return render(request,'Front.html')

def panel(request):
    return render(request,'panel.html')

def profile(request):
    about_me = {
        "my_page": "My name is Ghanem ",
        "email":"E-mail: ghanemxghanem@gmail.com",
        "numbers": 345,
        "mylist":[200,343,545,768]
    }
    return render(request,'profile.html',about_me)




