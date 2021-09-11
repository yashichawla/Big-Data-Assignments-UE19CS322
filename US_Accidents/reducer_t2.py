#!/usr/bin/env python3
import sys
a=sys.stdin.readline()
prev_state,prev_city,city_count=a.split(",")
prev_state=prev_state.strip()
prev_city=prev_city.strip()
city_count=1
state_count=1
print(prev_state)
for line in sys.stdin:
    state, city, count=line.split(",")
    state=state.strip()
    city=city.strip()
    count=count.strip()
    try:
        count = int(count)
    except ValueError:
        continue

    if prev_state==state:
        if prev_city==city:
            city_count+=1
            state_count+=1
        else: 
            print(prev_city, city_count)
            city_count=1
            prev_city=city
            state_count+=1
    else: 
        print(prev_state,state_count)
        print(state)
        state_count=1
        prev_state=state
        city_count=1
        prev_city=city
    
print(city,city_count)
print(state,state_count)