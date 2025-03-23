def convert(n,base):
    digits = "0123456789ABCDEF"
    if n == 0:
        return "0"
    result = ''
    while n>0:
        result = digits[n%base] + result
        n = n//base
    return result

def solution(n, t, m, p):
    temp = ''
    number = 0
    
    while len(temp) < t * m:
        temp += convert(number, n)
        number += 1

    answer = ''
    for i in range(t):
        answer += temp[(i * m) + (p - 1)]

    return answer
    
    
    

    return answer