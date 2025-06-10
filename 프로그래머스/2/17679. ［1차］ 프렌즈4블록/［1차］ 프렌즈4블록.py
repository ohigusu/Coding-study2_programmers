def solution(m, n, board):
    '''
    판의 높이: m
    폭: n
    판의 배치 정보: board
    '''
    total_removed = 0
    board = [list(row) for row in board]
    while True:
        to_remove = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == ' ':
                    continue
                if board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j] and board[i][j+1] == board[i+1][j+1]:
                    to_remove.update([(i, j), (i, j+1), (i+1, j), (i+1, j+1)])
        if not to_remove:
            break
        total_removed += len(to_remove)
        for i, j in to_remove:
            board[i][j] = ' '
        
        for j in range(n):
            empty = []
            for i in range(m-1,-1,-1):
                if board[i][j] == ' ':
                    empty.append(i)
                elif empty:
                    empty_i = empty.pop(0)
                    board[empty_i][j] = board[i][j]
                    board[i][j] = ' '
                    empty.append(i)
        

    return total_removed
