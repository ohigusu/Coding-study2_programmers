def factorial(n):
    result = 1
    for i in range(2,n+1):
        result *= i
    return result

def nCr(n, r):
    if r > n:
        return 0
    return factorial(n)//(factorial(r)*factorial(n-r))

N = int(input().strip())
answer = 0
if N%2: # 홀수
    end = ((N-1)//2)+1  
else:
    end = (N//2)+1 

for k in range(0,end):
    n,r = N-2*k,k
    answer += nCr(n+r,r)

print(answer%10007)