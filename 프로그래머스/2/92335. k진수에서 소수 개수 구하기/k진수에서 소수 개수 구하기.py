def convert(n,base):
    digits = '0123456789ABCDEF'
    result = ''
    
    while n > 0:
        result = digits[n%base]+result
        n = n//base
    return result 

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    words = convert(n, k)
    for part in words.split('0'):
        if part and is_prime(int(part)):
            answer += 1
    return answer