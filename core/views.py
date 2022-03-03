from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from . forms import ConDataForm
from core.models import Country_data
from django.http import HttpResponseRedirect
def HomeView(request):
    data = Country_data.objects.all()
    if request.method == 'POST':
        form = ConDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ConDataForm()
    return render(request, 'core/home.html',{'data':data,'form':form})


def updateView(request, pk):
    update_data = Country_data.objects.get(pk=pk)
    form = ConDataForm(request.POST, instance=update_data)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, "core/update.html", {'form':form ,'update_data':update_data})


def deleteView(request, pk):
    delete_data = Country_data.objects.get(pk=pk)
    if request.method == "POST":
        delete_data.delete()
        return redirect('/')
    return render (request, "core/delete.html",{'delete_data':delete_data})

