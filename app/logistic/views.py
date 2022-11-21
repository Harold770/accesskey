from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'logistic/home.html')
def myschedule(request):
    return render(request, 'logistic/myschedule.html')
