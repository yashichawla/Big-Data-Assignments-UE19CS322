#!/usr/bin/env python3
import json
import sys
from datetime import *
def checkConditions(data):
    conditions=["Description", "Severity","Sunrise_Sunset","Visibility(mi)","Precipitation(in)","Weather_Condition"]
    for i in conditions:
        if str(data[i])=="nan":
            return False
    desc=["lane blocked","shoulder blocked","overturned vehicle"]
    z=0
    for x in desc:
        if x not in data["Description"].lower():
            z+=1
    if z==3: 
        return False
    if(data["Severity"] < 2):
        return False
    if(data["Sunrise_Sunset"] != "Night"):
        return False
    if(data["Visibility(mi)"] > 10):
        return False
    if(data["Precipitation(in)"] < 0.2):
        return False
    weather=["Heavy Snow", "Thunderstorm", "Heavy Rain", "Heavy Rain Showers","Blowing Dust"]
    if data["Weather_Condition"] not in weather:
        return False
    return True

for line in sys.stdin:
    data = json.loads(line.strip())
    if checkConditions(data):
        time = datetime.strptime(data["Start_Time"], "%Y-%m-%d %H:%M:%S")
        print("{:d},1".format(time.hour))