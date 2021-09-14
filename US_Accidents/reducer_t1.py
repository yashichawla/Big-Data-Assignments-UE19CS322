#!/usr/bin/env python3
import sys
# hourCount = dict()

# for line in sys.stdin:
#     hour, count = line.split(",")
#     hour = int(hour.strip())
#     count = count.strip()

#     try:
#         count = int(count)
#     except ValueError:
#         continue

#     if hour not in hourCount.keys():
#         hourCount[hour] = 0
#     hourCount[hour] += count

# for hour in sorted(list(hourCount.keys())):
#     print(hour, hourCount[hour])

hourCount=[0 for i in range(0,24)]
for line in sys.stdin:
    hour, count = line.split(",")
    hour = int(hour.strip())
    count = count.strip()

    try:
        count = int(count)
    except ValueError:
        continue

    hourCount[hour]+=1

for h in range(len(hourCount)):
    if hourCount[h]>0:
        print(h,hourCount[h])

