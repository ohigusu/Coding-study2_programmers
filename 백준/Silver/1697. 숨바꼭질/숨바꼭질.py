from collections import deque
N,K = map(int,input().strip().split())

def bfs(N,K):
    visited = [-1]*100001
    queue = deque([N])
    visited[N] = 0

    while queue:
        x = queue.popleft()
        if x == K:
            return visited[x]
        for next_x in (x-1,x+1,2*x):
            if 0 <= next_x < 100001 and visited[next_x]==-1:
                visited[next_x] = visited[x]+1
                queue.append(next_x)

print(bfs(N,K))