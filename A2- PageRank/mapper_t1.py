#!/usr/bin/env python3
import sys
for line in sys.stdin:
    line=line.strip()
    try:
        source, dest=line.split()
        source=source.strip()
        dest=dest.strip()
    except:
        continue
    print(f"{source}\t{dest}")