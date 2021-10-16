#!/usr/bin/env python3
import sys
prev_page=0
sum=0
page=0
for line in sys.stdin:
    line=line.strip()
    try:
        page, contribution=line.split(" ")
        page=page.strip()
        contribution=float(contribution.strip())
    except:
        continue

    if prev_page==0:
        prev_page=page
        sum=contribution

    elif prev_page==page:
        sum+=contribution

    else: 
        print("{},{:.2f}".format(prev_page,0.15+0.85*sum)
        prev_page=page
        sum=contribution

print("{},{:.2f}".format(page,0.15+0.85*sum)
