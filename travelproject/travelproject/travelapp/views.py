from django.shortcuts import render
from . models import Place
from . models import Person

# Create your views here.
# def operations(request):
#    return render(request,"oper.html")

# def addition(request):
#    x=int(request.GET['num1'])
#    y=int(request.GET['num2'])
#    add=x+y
#    sub=x-y
#    mul=x*y
#    div=x/y
#    return render(request,"result.html",{'addi':add,'subt':sub,'multi':mul,'divi':div})

def demo(request):
    obj=Place.objects.all()
    per=Person.objects.all()
    return render(request,"index.html",{'result':obj,'out':per})