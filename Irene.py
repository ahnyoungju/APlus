# import requests
import json
import common

class ioT:
    def __init__(self, name = "ioT Device"):
        f = open("TodayWeather.json", "r")
        todayWeather = f.read()
        #todayWeather = common.decode(todayWeather)
        self.weather = json.loads(todayWeather)
     #   self.weather['Sunset'] = datetime.fromtimestamp(self.weather['Sunset'])
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
