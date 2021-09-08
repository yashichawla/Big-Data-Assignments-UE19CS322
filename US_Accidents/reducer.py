#!/usr/bin/env python
import sys
hourCount = dict()

for line in sys.stdin:
    hour, count = line.split("\t")
    hour = hour.strip()
    count = count.strip()

    try:
        count = int(count)
    except ValueError:
        continue

    if hour not in hourCount.keys():
        hourCount[hour] = 0
    hourCount[hour]+= count

for hour, count in hourCount.items():
    print("{}\t{}".format(hour, count))