#!/bin/env python3

import json, urllib.request
from os.path import expanduser


home = expanduser("~")

folderForFolder=open(home+"/Documents/git_projects/wunderWeather/folder");
folder = folderForFolder.read().rstrip("\n");
folderForFolder.close()


fileCurrent = open(folder + "current_condition")
fileHourly = open(folder + "hourly_forecast")
fileForecast = open(folder + "forecast")

current_condition = fileCurrent.read()
hourly_forecast = fileHourly.read();
forecast = fileForecast.read();

fileCurrent.close()
fileHourly.close()
fileForecast.close()




print("Downloading weather pictures...")

#current condition
values = json.loads(current_condition)
current = values["current_observation"]

#download image
pic = urllib.request.urlretrieve("http://icons.wxug.com/i/c/k/" + current["icon"] +".gif",  folder + "currentPic.gif")



#forecast
values = json.loads(forecast)
current = values["forecast"]["txt_forecast"]["forecastday"][0]


#download image
pic = urllib.request.urlretrieve("http://icons.wxug.com/i/c/k/" + current["icon"] +".gif",  folder + "forecast.gif")




#Hourly forecast
values = json.loads(hourly_forecast)

allTemps = values["hourly_forecast"]
for i in range(0, 14 ):
	print("http://icons.wxug.com/i/c/k/" + allTemps[i]["icon"] +".gif",  folder + "hour" + str(i) + ".gif");
	pic = urllib.request.urlretrieve("http://icons.wxug.com/i/c/k/" + allTemps[i]["icon"] +".gif",  folder + "hour" + str(i) + ".gif")






