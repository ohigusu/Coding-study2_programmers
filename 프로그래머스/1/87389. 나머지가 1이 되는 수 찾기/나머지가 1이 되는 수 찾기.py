def solution(n):
    
    d = n-1
    answer = d
    for i in range(2,int(d**0.5)+1):
        if d%i==0:
            answer = i
            break
    return answer