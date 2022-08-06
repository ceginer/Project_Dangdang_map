from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def cafeList(request):
    #
    #
    #
    return render(request, 'cafeList.html')

def accomodationList(request):
    #
    #
    #
    return render(request, 'accomodationList.html')

def placeList(request):
    #
    #
    #
    return render(request, 'placeList.html')