from unicodedata import category
from django.shortcuts import render, redirect

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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

def detail(request):
    #
    #
    #
    return render(request, 'detail.html')

def mainList(request):
    #
    #
    #
    return render(request, 'mainList.html')

@csrf_exempt
def locations(request):
    req = json.loads(request.body)
    location = req['location'] # 사용자가 선택한 location 값 (ajax)

    # 위에서 받은 location으로 data 분류해서 내보내기

    return JsonResponse({}) # 여기에 data 값들 넎어서 다시 보내기

@csrf_exempt
def cates(request):
    req = json.loads(request.body)
    cate = req['cate'] # 카페, 숙소, 장소
    return JsonResponse({'cate' : cate})

@csrf_exempt
def locationBtn(request):
    return JsonResponse({})

@csrf_exempt
def listGo(request):
    req = json.loads(request.body)
    location = req['location']
    category = req['category']
    detail = req['detail']

    # 여기서 data 처리해서 반환해주세요

    # 아래는 test용 JsonResponse 입니다. 수정필요
    return JsonResponse({'location' : location, 'category' : category, 'detail' : detail})
