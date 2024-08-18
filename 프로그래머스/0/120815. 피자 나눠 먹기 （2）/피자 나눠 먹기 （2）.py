def solution(n):
    
    for i in range(1,601):
        if (i*6) % n == 0:
            answer = i
            break
    return answer