from collections import deque
N, L, R = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

# 두 나라의 인구 차이가 L명 이상, R명 이하
# 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합
# 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
# 연합을 해체하고, 모든 국경선을 닫는다.
days = 0
dx,dy = [-1,1,0,0],[0,0,-1,1]
def bfs(sx,sy):
    queue = deque([(sx,sy)])
    union = [(sx,sy)]
    visited[sy][sx]=True
    population = graph[sy][sx]
    country_count = 1

    while queue:
        nx,ny = queue.popleft()
        for i in range(4):
            x,y= nx+dx[i],ny+dy[i]
            if 0 <= x < N and 0 <= y < N and not visited[y][x]:
                if L <= abs(graph[y][x]-graph[ny][nx]) <= R:
                    visited[y][x]= True
                    queue.append((x,y))
                    union.append((x,y))
                    population += graph[y][x]
                    country_count  += 1

    new_pop = population//country_count 

    for ux,uy in union:
        graph[uy][ux] = new_pop

    return len(union)>1

while True:
    visited = [[False]*N for _ in range(N)]
    move = False
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                if bfs(x,y):
                    move = True
    if not move:
        break
    days += 1

print(days)