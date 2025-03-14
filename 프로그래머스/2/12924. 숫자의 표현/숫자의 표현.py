def solution(n):
    answer = 0
    k = 1
    #n=a+(a+1)+(a+2)+...+(a+(k-1)) = k*a + k*(k-1)//2
    #(n-k*(k-1)//2)/k = a
    while k*(k-1)//2 < n:
        if (n-k*(k-1)//2)%k==0:
            answer += 1
        k += 1
    return answer