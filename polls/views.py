from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("홍준표가 좋으신가요 윤석렬이 좋으신가요?")