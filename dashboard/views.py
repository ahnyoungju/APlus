from django.shortcuts import render
import json
from Irene import ioT

# Create your views here.
def dashboard(request):
    #Read weather data
    i = ioT()
    devices = {}
    devices["umbrella"] = i.umbrella()
    devices["gardenwater"] = i.gardenwater()
    devices["weather"] = i.weather

    #Read News Data
    f = open("NewsData.json", "r")
    newsdata = f.read()
    f.close()
    newsdata = json.loads(newsdata)
    devices["News"] = newsdata

    #Read Shopping List
    f = open("ShoppingList.json", "r")
    slist = eval(f.read())
    f.close()
    devices["ShoppingList"] = slist

    return render(request,'main.html', {'ioT': devices})
