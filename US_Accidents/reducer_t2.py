#!/usr/bin/env python3
import sys
stateCount=dict()
for line in sys.stdin:
    state, city, count=line.split(",")
    state=state.strip()
    city=city.strip()
    count=count.strip()
    try:
        count = int(count)
    except ValueError:
        continue
    if state not in stateCount.keys():
        stateCount[state]=dict()
    if city not in stateCount[state].keys():
        stateCount[state][city]=0
    stateCount[state][city]+=1

for state in sorted(list(stateCount.keys())):
    print(state)
    state_count=0
    cityCount=stateCount[state]
    for city in sorted(list(cityCount.keys())):
        print(city,cityCount[city])
        state_count+=cityCount[city]
    print(state, state_count)
