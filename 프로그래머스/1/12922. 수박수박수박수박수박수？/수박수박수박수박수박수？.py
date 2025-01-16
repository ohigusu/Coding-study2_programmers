def solution(n):
    return '수박'*((n-1)//2)+'수' if n%2 else '수박'*(n//2)
# "수박" * (n//2) + "수" * (n%2)