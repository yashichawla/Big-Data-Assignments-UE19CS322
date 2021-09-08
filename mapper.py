import json
from datetime import *
f = open("US_ACCIDENT_DATA_5PERCENT.json")


def checkConditions(data):
    # check for NaN for all 6 attributes, move to next line
    desc = data["Description"]
    # optimizie desc condition
    if(("lane blocked" not in desc) and ("shoulder blocked" not in desc) and ("overturned vehicle" not in desc)):
        return False
    if(data["Severity"] <= 2):
        return False
    if(data["Sunrise_Sunset"] != "Night"):
        return False
    if(data["Visibility(mi)"] <= 10):
        return False
    if(data["Precipitation(in)"] <= 0.2):
        return False
    # weather condition
    return True


i = 0
for line in f:
    data = json.loads(line.strip())
    if checkConditions(data):
        time = datetime.strptime(data["Start_Time"], "%Y-%m-%d %H:%M:%S")
        print("{:d}".format(time.hour))
        i += 1
        # if i>=10: break
print("COUNT", i)
