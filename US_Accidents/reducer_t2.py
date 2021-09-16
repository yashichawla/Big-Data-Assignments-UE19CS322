#!/usr/bin/env python3
import sys

prev_state=None
prev_city=None
city_count=0
state_count=0

for line in sys.stdin:
    state, city, count=line.split(",")
    state=state.strip()
    city=city.strip()
    count=count.strip()
    try:
        count = int(count)
    except ValueError:
        continue

    if prev_state==None and prev_city==None:
        print(state)
        prev_state=state
        prev_city=city
        city_count=1
        state_count=0

    elif prev_state==state:
        if prev_city==city:
            city_count+=1
        else: 
            print(prev_city, city_count)
            state_count+=city_count
            city_count=1
            prev_city=city
    else: 
        print(prev_city,city_count) #missing condition
        state_count+=city_count
        print(prev_state,state_count)
        print(state)
        prev_state=state
        city_count=1
        prev_city=city
        state_count=0

print(prev_city,city_count)
state_count+=city_count
print(prev_state,state_count)