def dfs(graph, visited, start):
    stack = [start]
    visited[start] = True
    while stack:
        node = stack.pop()
        next_node = graph[node]
        if not visited[next_node]:
            visited[next_node] = True
            stack.append(next_node)
                

def cnt_cycle(n,graph):
    visited = [False]*(n+1)
    cnt = 0
    for i in range(1,n+1):
        if not visited[i]:
            dfs(graph,visited,i)
            cnt += 1
    return cnt

T = int(input().strip())
results = []

for _ in range(T):
    n = int(input().strip())
    graph = [0]+list(map(int,input().strip().split()))
    result = cnt_cycle(n,graph)
    results.append(result)

for res in results:
    print(res)

