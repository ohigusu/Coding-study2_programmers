from collections import defaultdict
import sys
import bisect

N = int(sys.stdin.readline().strip())  
res = defaultdict(list)

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    bisect.insort(res[x], y)  

for x in sorted(res.keys()): 
    for y in res[x]:  
        print(f"{x} {y}")