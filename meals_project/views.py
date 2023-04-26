from django.shortcuts import render
from django.http import HttpResponse
from .forms import *


# def information(request):
#     if request.method == 'GET':
#         form = Info()
#         return render(request, 'main.html', {'form': form})
#     if request.method == 'POST':
#         form = Info(request.POST)
#         info = form.save()
#         #return HttpResponse('Form submission successful!')
#         return render(request, 'success.html')
#     return render(request, 'main.html', {'form': form})

def information(request):
    form = Info()
    if request.method == 'GET':
        return render(request, 'main.html', {'form': form})
    if request.method == 'POST':
        form = Info(request.POST)
        if form.is_valid():
            info = form.save()
            return render(request, 'success.html')
    return render(request, 'main.html', {'form': form})
    # form = Info(request.POST)
    # book = form.save()
    # return render(request,'main.html',{'form': form})

# Create your views here.
