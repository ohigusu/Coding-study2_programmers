def solution(board):
    answer = 0
    result = []
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                result.append([i,j])
    for coor in result:
        x,y = coor
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if 0 <= i < n and 0 <= j < n:
                    board[i][j]=1  
    for b in board:
        answer += b.count(0)
    return answer