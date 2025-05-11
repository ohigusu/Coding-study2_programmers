from collections import deque
N,M = map(int,input().split())
graph = [list(map(int,input().strip())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(sx,sy,N,M,visited,graph):
    queue = deque([(sx,sy)])
    visited[sy][sx]=True
    while queue:
        nx,ny = queue.popleft()
        for i in range(4):
            x,y=nx+dx[i],ny+dy[i]
            if 0<=x<M and 0<=y<N:
                if not visited[y][x] and graph[y][x]==1:
                    visited[y][x]=True
                    queue.append((x,y))
                    graph[y][x] = graph[ny][nx]+1
    return graph

result = bfs(0,0,N,M,visited,graph)
print(result[N-1][M-1])
