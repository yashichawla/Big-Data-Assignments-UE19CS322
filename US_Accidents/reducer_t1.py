#!/usr/bin/env python3
import sys
hourCount = dict()

for line in sys.stdin:
    hour, count = line.split(",")
    hour = int(hour.strip())
    count = count.strip()

    try:
        count = int(count)
    except ValueError:
        continue

    if hour not in hourCount.keys():
        hourCount[hour] = 0
    hourCount[hour] += count

for hour in sorted(list(hourCount.keys())):
    print(hour, hourCount[hour])
