import sys
input = sys.stdin.readline

N, M = map(int,input().split())
hash_map ={}
for i in range(1,N+1):
    name = input().strip()
    hash_map[name] = i
    hash_map[str(i)] = name

for _ in range(M):
    u = input().strip()
    print(hash_map[u])