def solution(balls, share):
    up,down = 1,1
    while share:
        up = up*(balls)
        down = down*share
        share, balls = share - 1, balls-1
    answer = up/down
    return answer