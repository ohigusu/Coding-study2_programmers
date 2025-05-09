N = int(input().strip())
K = int(input().strip())

graph = [[] for _ in range(N+1)]


for _ in range(K):
    a,b = map(int,input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

visited =[False]*(N+1)

def dfs(start):
    cnt = 0
    stack = [start]
    visited[start]=True
    while stack:
        node = stack.pop()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node]=True
                cnt += 1
                stack.append(next_node)
    return cnt


if len(graph[1])>0:
    cnt = dfs(1)
else:
    cnt = 0

print(cnt)