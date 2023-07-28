 

from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

class NewMenuForm(forms.Form):
    menu = forms.CharField(label="Add menu")
# Create your views here.
def index(request):
    if "msosi_list" not in request.session:
        request.session["msosi_list"]= []
    return render( request, "msosi/index.html", {
        "msosi": request.session ["msosi_list"]
    })

def add(request):
    if request.method=="POST":
        form = NewMenuForm(request.POST)
        if form.is_valid():
           menu=form.cleaned_data["menu"]
           request.session ["msosi_list"] += [menu]
           return HttpResponseRedirect(reverse ("index"))
        
        else:
            return render( request, "msosi/add.html", {
                "form": form
            })
    return render(request, "msosi/add.html", {
        "form": NewMenuForm()
    })
