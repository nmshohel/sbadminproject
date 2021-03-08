from django.shortcuts import render,HttpResponse

# Create your views here.
def home_page(request):
    return render(request, 'home_page.html')

def user_login(request):
    return render(request, 'user_login.html')
    