# import requests
import json
import common
import base64

class ioT:
    def __init__(self, name = "ioT Device"):
        f = open("TodayWeather.json", "r")
        todayWeather = common.decode(f.read())
        self.weather = json.loads(todayWeather)
        f.close()
        self.name=name
        print(self.weather)

    def umbrella(self):
        if self.weather['Humidity'] > 50 :
            return True
        else:
            return False

    def gardenwater(self):
        if self.weather['Humidity'] > 70 :
            return True
        else:
            return False
