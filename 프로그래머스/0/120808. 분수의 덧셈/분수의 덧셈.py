def solution(numer1, denom1, numer2, denom2):
    import math
    up = numer1*denom2 + numer2*denom1
    down = denom1*denom2
    gcd = math.gcd(up,down)
    answer = [up//gcd,down//gcd]
    return answer