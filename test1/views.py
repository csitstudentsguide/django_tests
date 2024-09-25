from django.shortcuts import render
from django.http import HttpResponse
from .forms import Test1Form

# Create your views here.
def test1_home(request):
    form =  Test1Form()    
    return render(request, 'test1/test1_home.html', {form:form})
