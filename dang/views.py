from asyncio.windows_events import NULL
from http.client import HTTPResponse
from unicodedata import category
from django.shortcuts import render, redirect,HttpResponse
import csv

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import User, Location, Cafe, Place, Accomodation, Medical, Post 

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





### db에 csv 파일 넣는 함수입니다.
### migrations 날리고 dbsqlite 날리고 사용해야 합니다. 한번만 작동해주세요..!! 여러번 하면 여러번 들어가요
def csvToModel(request):
    c = open("./static/csv/cafe.csv",'r',encoding='CP949')
    a = open("./static/csv/accommo.csv",'r',encoding='CP949')
    p = open("./static/csv/place.csv",'r',encoding='CP949')
    
    reader_cafe = csv.reader(c)
    reader_accomo = csv.reader(a)
    reader_place = csv.reader(p)

    cafes = []
    places = []
    accomos = []

    for row in reader_accomo:
        accomos.append(Accomodation(accomodationName=row[0],location=row[1],accomodationAddress=row[2],accomodationPhone=row[3],accomodationStar=row[4],accomodationLink1=row[5],accomodationLink2=row[6],accomodationType=row[7],accomodationDesc=row[8],accomodationImg=row[9][0],accomodationMapx=row[10],accomodationMapy=row[11]))
    Accomodation.objects.bulk_create(accomos)

    for r in reader_cafe:
        try:
            cafes.append(Cafe(cafeName=r[0],location=r[1],cafeAddress=r[2],cafePhone=r[3],cafeType=r[4],menuInfo=r[5],hourInfo=r[6],cafeLink1=r[7],cafeDesc=r[8],cafeImg=r[9],cafeMapx=r[10],cafeMapy=r[11]))
        except:
            cafes.append(Cafe(cafeName=r[0],location=r[1],cafeAddress=r[2],cafePhone=r[3],cafeType=r[4],menuInfo=r[5],hourInfo=r[6],cafeLink1=r[7],cafeDesc=r[8],cafeImg=r[9]))
    Cafe.objects.bulk_create(cafes)

    for r in reader_place:
        places.append(Place(placeName=r[0],location=r[1],placeAddress=r[2],placePhone=r[3],placeStar=r[4],placeLink1=r[5],placeLink2=r[6],placeType=r[7],placeDesc=r[8],placeImg=r[9],placeMapx=r[10],placeMapy=r[11]))
    Place.objects.bulk_create(places)


    c.close()
    a.close()
    p.close()

    return HttpResponse('create model~')