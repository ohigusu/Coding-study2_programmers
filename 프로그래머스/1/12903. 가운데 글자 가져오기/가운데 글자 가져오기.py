def solution(s):
    answer = ''
    n = len(s)
    if n%2 == 0:
        mid = n//2
        answer = s[mid-1:mid+1]
    else:
        answer = s[n//2]
    return answer