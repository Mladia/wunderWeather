#!/bin/env python

import json, urllib.request, sys
from os.path import expanduser


try:
	parameter = int(sys.argv[1])
except IndexError:
	print('For current condition, please use the parameter "0"; for hourly forecast, the parameter "1"; for full text, the parameter 3,  eg. wed.py 0')
	sys.exit()


#TODO: read folder from the file 'folder' 
home = expanduser("~")
folder= home+"/.cache/wunderWeather/"

fileCurrent = open(folder + "current_condition")
fileForecast = open(folder + "forecast")
fileHourly = open(folder + "hourly_forecast")

current_condition = fileCurrent.read()
forecast = fileForecast.read()
hourly_forecast = fileHourly.read();

fileCurrent.close()
fileHourly.close()
fileForecast.close()


#current condition
values = json.loads(current_condition)

current=values["current_observation"]


#weatherText
weatherText = current["weather"]


#temp
currTemp = current["temp_c"]

precip = current["precip_1hr_metric"]


#Text description
values = json.loads(forecast)
current = values["forecast"]
te_descr = current["txt_forecast"]["forecastday"][0]["fcttext_metric"]




if parameter==0:
	print("Now is " + str(currTemp) + " C, " + weatherText + ", " +  " precip: "+ precip );
	sys.exit()

elif parameter==3:
	print("Now is " + str(currTemp) + " C, " + te_descr);
	sys.exit()
	



#Hourly forecast
values = json.loads(hourly_forecast)

allTemps = values["hourly_forecast"]



#temp[hour][weatherText][pop]
temps =  []

for i in range(0, 14):
	
	time = allTemps[i]["FCTTIME"]["hour_padded"] + ":" + allTemps[i]["FCTTIME"]["min"] + "-" + allTemps[i]["FCTTIME"]["mday_padded"] +"-"+ allTemps[i]["FCTTIME"]["mon_abbrev"]

	temp = allTemps[i]["temp"]["metric"]
	condition = allTemps[i]["condition"]
	pop = allTemps[i]["pop"]
	print(time + " is " + str(temp) + " C" + ", " + condition +", rain: " + str(pop) + "%"  )
#	temps[i] = (time, condition, pop0




#https://stackoverflow.com/questions/13246597/how-to-read-a-file-line-by-line-in-php
