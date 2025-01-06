def solution(s):
    answer = 0
    if s[0] == '-':
        answer = -int(s[1:])
    answer = int(s)
    return answer