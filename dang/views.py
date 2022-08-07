from asyncio.windows_events import NULL
from unicodedata import category
from django.shortcuts import render, redirect

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# 임시로 만들어 둔 지역 list입니다. 나중에 db로 대체하든, 얘기해봐요..
locationDic = {'seoul':'서울','gyeongi':'경기','incheon':'인천','gangwon':'강원','chungbuk':'충북','chungnam':'충남','deajeon':'대전','sejong':'세종','jeonbuk':'전북','jeonnam':'전남','gwangju':'광주','gyeongbuk':'경북','gyeongnam':'경남','daegu':'대구','ulsan':'울산','busan':'부산','daejeon':'대전','jeju':'제주' }

def home(request):
    locationList = locationDic.values()

    context = { "locationList" : locationList }

    return render(request,'home.html', context=context)

def cafeList(request):
    #
    context = { "category" : "cafe", "location" : NULL}
    #
    #
    return render(request, 'mainList.html', context=context)

def placeList(request):
    #
    context = { "category" : "place", "location" : NULL }
    #
    #
    return render(request, 'mainList.html', context=context)

def accomoList(request):
    #
    context = { "category" : "accomo", "location" : NULL }
    #
    #
    return render(request, 'mainList.html', context=context)

def mainList(request, location): # main에서 지역 선택했을 때
    #
    context = { "location" : location }
    #
    #
    return render(request, 'mainList.html', context=context)

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
