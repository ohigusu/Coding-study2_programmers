def solution(n):
    root = n**(1/2)
    if root % 1 == 0:
        return 1
    else:
        return 2
