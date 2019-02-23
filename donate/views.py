from django.shortcuts import render, redirect


# Create your views here.


#return to home page
def index(request):
    return redirect('home/')



#home page view
def home(request):


    return render(request , 'home.html')