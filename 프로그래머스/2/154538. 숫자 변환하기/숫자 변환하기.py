from collections import deque
def solution(x, y, n):
    if x == y:
        return 0
    dist = [-1]*(y+1)
    dist[x] = 0
    q = deque([x])
    while q:
        cur = q.popleft()
        cur_dist = dist[cur]
        
        for nxt in (cur+n,cur*2,cur*3):
            if nxt > y:
                continue
            if dist[nxt] != -1:
                continue
            dist[nxt] = cur_dist + 1
            if y == nxt:
                return dist[nxt]
            q.append(nxt)
    return -1
