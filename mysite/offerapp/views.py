from django.shortcuts import render
from django.http import HttpResponse

def index(request) :
	return HttpResponse("<h2>HEYYY</h2>")
# Create your views here.
