from collections import deque

def solution(board):
    h = len(board)
    w = len(board[0])
    visited = [[False]*w for _ in range(h)]
    
    # 방향: 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 시작점(R) 찾기
    for i in range(h):
        for j in range(w):
            if board[i][j] == 'R':
                start = (i, j)
                break
    
    q = deque()
    q.append((start[0], start[1], 0))  # x, y, 이동횟수
    visited[start[0]][start[1]] = True

    while q:
        x, y, cnt = q.popleft()
        
        if board[x][y] == 'G':
            return cnt
        
        for d in range(4):
            nx, ny = x, y
            # 리코쳇처럼 끝까지 이동
            while True:
                tx = nx + dx[d]
                ty = ny + dy[d]
                if 0 <= tx < h and 0 <= ty < w and board[tx][ty] != 'D':
                    nx, ny = tx, ty
                else:
                    break
            
            # 이미 방문한 곳이면 생략
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, cnt + 1))

    return -1          
        
        
    
    return answer