#!/bin/env python

import requests, json, urllib.request
from datetime import datetime

file = open('key', 'r')
key = file.read().rstrip("\n").rstrip(" ")

file.close()



urlTemp="http://api.wunderground.com/api/" + key + "/hourly/q/zmw:00000.61.10267.json"



fromUrlTemp=""
fromUrlTemp = urllib.request.urlopen(urlTemp).read();
values = json.loads(fromUrlTemp)

allTemps = values["hourly_forecast"]
for i in range(0, len(allTemps) ):
	
	time = allTemps[i]["FCTTIME"]["pretty"]

	temp = allTemps[i]["temp"]["metric"]
	condition = allTemps[i]["condition"]
	pop = allTemps[i]["pop"]
	print("At time "+ time + " is " + str(temp) + " C" + " with " + condition +", rain: " + str(pop) + "%"  )






