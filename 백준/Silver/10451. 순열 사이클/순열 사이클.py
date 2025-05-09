def find_cycle(graph, visited, start):
    stack = [start]
    while stack:
        node= stack.pop()
        if not visited[node]:
            visited[node] = True
            stack.append(graph[node])

def count_cycles(n,permutation):
    visited = [False]*(n+1)
    cycle_count = 0

    for i in range(1,n+1):
        if not visited[i]:
            find_cycle(permutation, visited, i)
            cycle_count += 1
    return cycle_count

t = int(input())
results = []

for _ in range(t):
    n = int(input().strip())
    permutation = [0]+list(map(int,input().strip().split()))
    result = count_cycles(n,permutation)
    results.append(result)

for res in results:
    print(res)
