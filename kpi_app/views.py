from django.shortcuts import render

# Create your views here.
def home(request):
    # You can pass data to the template here
    return render(request, "home.html")