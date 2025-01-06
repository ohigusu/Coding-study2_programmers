def solution(n):
    answer = 0
    cnt = len(str(n)) #3
    i=1
    now = 10**(cnt-1) #100
    while i <= cnt:
        answer += n//now 
        n = n%now 
        now = now//10
        i += 1 
    return answer