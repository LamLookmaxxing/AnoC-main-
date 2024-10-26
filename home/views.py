from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def services(request):
    return render(request, 'home/services.html')

def projects(request):
    return render(request, 'home/projects.html')

def blog(request):
    return render(request, 'home/blog.html')

def pricing(request):
    return render(request, 'home/pricing.html')

def contact(request):
    return render(request, 'home/contact.html')

def payment(request):
    return render(request, 'home/payment.html')