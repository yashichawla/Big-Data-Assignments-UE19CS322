#!/usr/bin/env python3
import sys
source=0
dest=0
adj_list=list()
prev_source=0

dir=sys.argv[1].strip()
v= open(dir, "w")

for line in sys.stdin:
    try:
        line=line.strip()
        source,dest=line.split("\t")
        source=int(source.strip())
        dest=int(dest.strip())
    except:
        continue
    
    if prev_source==0:
        prev_source=source
        adj_list.append(dest)

    elif prev_source==source:
        adj_list.append(dest)

    else: 
        print(prev_source,adj_list) #write to adj_list file in hdfs, prev_source,1 to v file
        v.write(f"{prev_source}, 1\n")
        prev_source=source
        adj_list=list()
        adj_list.append(dest)

print(source,adj_list)
v.write(f"{prev_source}, 1\n")
#LAST SOURCE write to adj_list file in hdfs, prev_source,1 to v file