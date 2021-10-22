from django.shortcuts import render,redirect

# Create your views here.
from .models import Article


def Article_details(request):
    obj = Article.objects.get(id=1)
    context={
        'object':obj
    }
    return render(request,"article_detail.html",context)


def delete(request,my_id):
    obj = Article.objects.get(id=my_id)
    if request.POST:#if the user selects yes, delete the object
        print("delete")
        obj.delete()
        return redirect('../../')
    context = {
        'object':obj
    }
    return render(request, "product/delete.html", context)
