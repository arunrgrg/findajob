from django.shortcuts import render


def homefun(request):
    return render(request,'home.html')