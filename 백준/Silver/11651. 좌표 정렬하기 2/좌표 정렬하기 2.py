import sys

N = int(sys.stdin.readline())
res = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    res.append((x, y))

sorted_res = sorted(res, key=lambda x: (x[1], x[0]))

for i in sorted_res:
    print(f"{i[0]} {i[1]}")