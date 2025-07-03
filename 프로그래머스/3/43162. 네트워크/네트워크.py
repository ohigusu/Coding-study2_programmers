def solution(n,computers):
    visited = [False]*n

    def dfs(node):
        visited[node] = True
        for v in range(n):
            if computers[node][v] == 1 and not visited[v]:
                #visited[v] = True
                dfs(v)
    cnt = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            cnt += 1
    return cnt
