from django.shortcuts import render

# Create your views here.
def Home(request):
    context = {}
    return render(request, 'home/index.html', context)

def About(request):
    context = {}
    return render(request, 'home/about_us.html', context)

def Demo(request):
    context = {}
    return render(request, 'home/demo.html', context)

def Price(request):
    context = {}
    return render(request, 'home/price.html', context)

def Contact(request):
    context = {}
    return render(request, 'home/contact.html', context)

def Pedigree(request):
    context = {}
    return None