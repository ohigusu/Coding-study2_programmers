from collections import deque
F, S, G, U, D = map(int,input().split())
# F층으로 이루어진 고층 건물
# G층: 스타트링크가 있는 곳의 위치
# S층: 강호가 지금 있는 곳
# U버튼: 위로 U층을 가는 버튼
# D버튼: 아래로 D층을 가는 버튼
visited = [False] * (F + 1) 

def bfs(start_node):
    queue = deque([(start_node,0)])
    visited[start_node] = True
    while queue:
        node,cnt = queue.popleft()
        if node == G:
            return cnt

        next_up,next_down = node + U, node - D
        next = [next_up,next_down]
        for next_node in next:
            if 1 <= next_node <= F and not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node,cnt+1))
    return "use the stairs"
        
if S==G:
    print(0)
else:
    print(bfs(S))