def solution(s):
    n,mid = len(s),len(s)//2
    return s[mid-1:mid+1] if n%2 == 0 else s[n//2]