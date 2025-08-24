from django.shortcuts import render

def welcome_view(request):
    return render(request, 'my_canteen/welcome.html')
