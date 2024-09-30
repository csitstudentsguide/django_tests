from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Test1Form

# Create your views here.
def test1_home(request):        
    if request.method == 'POST':
        form = Test1Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Done')
    else:
        form = Test1Form()

    return render(request, 'test1/test1_home.html', {'form':form})
