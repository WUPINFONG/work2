from django.shortcuts import render

# Create your views here.
def abouts(request):
    return render(request,'abouts.html')