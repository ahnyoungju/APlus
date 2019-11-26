from Irene import ioT

i = ioT()
devices = {}
devices["umbrella"] = i.umbrella()
devices["gardenwater"] = i.gardenwater()
devices["weather"] = i.weather

print(i)