from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from .forms import NameForm, CreateBioLower14, CreateBioUpper14
from .models import GetInfor, CCCD, Queue
import datetime
from datetime import timedelta
import calendar
from .generator import queuegenerator, queueextractor, stringlizing
# Create your views here.

def index(response):
    """
    if response.method == "POST":
        if response.POST.get("save"):
            na=response.POST.get('gender')
        
            return render(response, 'temps/t.html', {'text': na})
    """
    return render(response, 'temps/index.html', {})

def camera(response):
    return render(response, 'temps/category.html', {})



def tokhaithongtin(response):
    return render(response, 'temps/tokhaithongtin.html', {})
        
def t(response):
    return render(response, 'temps/t.html', {})