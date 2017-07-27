#!/bin/env python

import json, urllib.request

from os.path import expanduser


home = expanduser("~")
folder= home+"/.cache/wunderWeather/currentForecast/"

fileCurrent = open(folder + "current_condition")
fileHourly = open(folder + "hourly_forecast")

current_condition = fileCurrent.read()
hourly_forecast = fileHourly.read();

fileCurrent.close()
fileHourly.close()



#current condition
values = json.loads(current_condition)

current=values["current_observation"]
#download the image

#weatherText
weatherText = current["weather"]


#temp
currTemp = current["temp_c"]


print("Now is " + str(currTemp) + " C, " + weatherText + ", " +  " precip: "+current["precip_1hr_metric"] );



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
	temps.append( (time, temp,  condition, pop))




print(temps[5])
