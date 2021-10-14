#!/usr/bin/env python3
import sys
import json
import math

def similarity(p,q):
    sum_p=0
    sum_q=0
    mag_p=0
    mag_q=0
    for i in p:
        sum_p+=pow(i,2)
    mag_p=math.sqrt(sum_p)

    for i in q:
        sum_q+=pow(i,2)
    mag_q=math.sqrt(sum_q)

    product=0
    for a,b in zip(p,q):
        product=product+ a*b
    
    product=product/(mag_p*mag_q)

    return product
    
pagerank=dict()

f=sys.argv[2].strip()
file=open(f)
emb=json.load(file)

dir=sys.argv[1].strip()
v= open(dir, "r+")

#get page ranks from v file

lines = v.read().strip().split("\n")
for line in lines:
    try:
        page, rank = line.split(",")
    except:
        continue
    pagerank[page.strip()] = float(rank.strip())

#get adj list and update contributions 
#print 0 by default - in case no node has incoming nodes to it
for line in sys.stdin:
    line=line.strip()
    source,adj_list=line.split("\t")

    source=source.strip()
    adj_list=eval(adj_list.strip())
    
    # print(line)
    number=len(adj_list)
    print(source,0)
    # vector value of source from embeddings
    p=emb[str(source)]
    for i in adj_list:
     #vector value of this node from embeddings
        q=emb[str(i)]
        sim=similarity(p,q)
        contribution=pagerank[source]*sim/number
        print(i,contribution)


