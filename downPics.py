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


print("Downloading weather pictures...")
#download image
pic = urllib.request.urlretrieve("http://icons.wxug.com/i/c/k/" + current["icon"] +".gif",  folder + "currentPic.gif")





#Hourly forecast
values = json.loads(hourly_forecast)

allTemps = values["hourly_forecast"]
for i in range(0, len(allTemps) ):
	pic = urllib.request.urlretrieve("http://icons.wxug.com/i/c/k/" + allTemps[i]["icon"] +".gif",  folder + "hour" + allTemps[i]["FCTTIME"]["civil"].replace(" ", "") + ".gif")






