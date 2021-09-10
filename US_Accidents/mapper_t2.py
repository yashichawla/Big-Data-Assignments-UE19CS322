#!/usr/bin/env python3
import json
import sys
import math
import requests

def euclideanDistance(lat,lng,d_lat,d_lng):
    return math.dist([lat,lng],[d_lat,d_lng])

lat=float(sys.argv[1])
lng=float(sys.argv[2])
d=float(sys.argv[3])

for line in sys.stdin:
    record=json.loads(line.strip())
    d_lat=record["Start_Lat"]
    d_lng=record["Start_Lng"]
    coordinates={"latitude":d_lat,"longitude":d_lng}
    distance=euclideanDistance(lat,lng,d_lat,d_lng)
    if distance <d:
        x=requests.post('http://20.185.44.219:5000/',json=coordinates)
        #state city 1
        new=x.json()
        print("{},{},{:d}".format(new["state"],new["city"],1))
    