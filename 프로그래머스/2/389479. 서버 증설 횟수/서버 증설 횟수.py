from collections import deque
import math

def solution(players, m, k):
    answer = 0               
    rest_time = deque()   
    n = 0                   

    for idx, value in enumerate(players):
        while rest_time and rest_time[0] <= idx:
            rest_time.popleft()
            n -= 1

        need = value // m

        if n < need:
            delta = need - n
            answer += delta
            n += delta
            expire_time = idx + k
            for _ in range(delta):
                rest_time.append(expire_time)
    return answer