from django.shortcuts import render,redirect
from .models import Laptop
from .forms import LaptopModelForm

# Create your views here.

def testView(request):
    template_name = 'base.html'
    context = {}
    return render(request,template_name,context)


def addOrderView(request):
    form = LaptopModelForm()
    if request.method == 'POST':
        form = LaptopModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showorders')
    template_name = 'addorder.html'
    context = {'form': form}
    return render(request, template_name, context)


def showOrderView(request):
    template_name = 'showorder.html'
    lap = Laptop.objects.all()
    context = {'lap':lap}
    return render(request,template_name,context)


def updateOrderView(request,id_from_fe):
    lap = Laptop.objects.get(id=id_from_fe)
    form = LaptopModelForm(instance=lap)
    if request.method =='POST':
        form = LaptopModelForm(request.POST,instance=lap)
        if form.is_valid():
            form.save()
            print('updated')
            return redirect('showorders')
    template_name = 'addorder.html'
    context = {'form':form}
    return render(request,template_name,context)


def deleteOrderView(request,id_from_fe):
    lap = Laptop.objects.get(id=id_from_fe)
    lap.delete()
    print('deleted')
    return redirect('showorders')    
            


