def check(x,y,l,board):
    x,y=x-1,y-1
    for i in range(x,x+3):
        for j in range(y,y+3):
            if 0<=i<l and 0<=j<l:
                board[i][j]=1  

def solution(board):
    answer = 0
    coor = []
    l = len(board)
    for i in range(l):
        for j in range(l):
            if board[i][j] == 1:
                coor.append([i,j])
    for c in coor:
        x,y=c
        check(x,y,l,board)

    print(board)

    for b in board:
        answer += b.count(0)

    return answer