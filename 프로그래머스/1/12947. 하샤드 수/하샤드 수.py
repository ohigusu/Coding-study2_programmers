def solution(x):
    answer = True
    li = list(str(x))
    su = 0
    for i in li:
        su += int(i)
    if x%su == 0:
        answer
    else:
        answer =False
    return answer