def solution(numer1, denom1, numer2, denom2):
    import math
    up = numer1*denom2 + numer2*denom1
    down = denom1*denom2
    for j in range(min(up,down),0,-1):
        if up%j==0 and down%j==0:
            gcd = j
            break
    answer = [up//gcd,down//gcd]
    return answer
