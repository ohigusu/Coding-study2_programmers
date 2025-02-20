def solution(board, moves):
    # 게임 화면의 격자의 상태가 담긴 2차원 배열 board
    # 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves
    [[0,0,0,0,0],
     [0,0,1,0,3],
     [0,2,5,0,1],
     [4,2,4,4,2],
     [3,5,1,3,1]]
    answer = 0
    stack = []
    for move in moves:
        col=move-1
        for row in range(len(board)):
            if board[row][col] != 0:
                picked = board[row][col]
                board[row][col] = 0  # 인형 제거
                if stack and stack[-1] == picked:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(picked)
                break
                        
    return answer