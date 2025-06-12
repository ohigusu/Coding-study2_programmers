def solution(n):
    answer = []
    tr = [[0]*i for i in range(1,n+1)]
    last_num = n*(n+1)//2
    dx,dy = [1,0,-1],[0,1,-1]
    direction = x = y = 0
    for i in range(1,last_num+1):
        tr[x][y] = i
        nx = x+dx[direction]
        ny = y+dy[direction]
        
        # 옆으로 가기, 내려가기, 위로 가기
        if nx >= n or nx < ny or tr[nx][ny] != 0: 
        # if not (0 <= nx < n and 0 <= ny <= nx and tr[nx][ny] == 0):
            direction = (direction + 1)%3
            nx = x+dx[direction]
            ny = y+dy[direction]
        x, y = nx, ny
    for row in tr:
        answer.extend(row)
    return answer
