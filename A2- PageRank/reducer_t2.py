#!/usr/bin/env python3

# page contribution
import sys
prev_page=0
sum=0
page=0
# dir=sys.argv[1].strip()
# v1= open(dir, "w")

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
        print(f"{prev_page},{round((0.15+0.85*sum),2)}")
        # v1.write(prev_page,0.15+0.85*sum) 
        prev_page=page
        sum=0

print(f"{page},{round(0.15+0.85*sum,2)}")
# v1.write(page,0.15+0.85*sum)