#!/bin/env python

import json, urllib.request


folder='~/.cache/wunderWeather/.currentForecast'

fileCurrent = open(folder + "/current_condition")
fileHourly = open(folder + "/hourly_forecast")

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

#download image
pic = urllib.request.urlretrieve("http://icons.wxug.com/i/c/k/" + current["icon"] +".gif",  "./.currentForecast/currentPic.gif")

print("Now is "+ weatherText + ", " + str(currTemp) + " C" + " precip: "+current["precip_1hr_metric"] );



#Hourly forecast
values = json.loads(hourly_forecast)

allTemps = values["hourly_forecast"]
for i in range(0, len(allTemps) ):
	
	time = allTemps[i]["FCTTIME"]["pretty"]

	temp = allTemps[i]["temp"]["metric"]
	condition = allTemps[i]["condition"]
	pop = allTemps[i]["pop"]
	print("At time "+ time + " is " + str(temp) + " C" + " with " + condition +", rain: " + str(pop) + "%"  )
	pic = urllib.request.urlretrieve("http://icons.wxug.com/i/c/k/" + allTemps[i]["icon"] +".gif",  "./.currentForecast/hourl" + allTemps[i]["FCTTIME"]["civil"].replace(" ", "") + ".gif")






