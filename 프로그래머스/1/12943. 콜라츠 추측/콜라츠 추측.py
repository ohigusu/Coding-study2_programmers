def solution(num):
    answer = 0
    result = num
    while result != 1 and answer < 500:
        if result % 2==0:
            result = result/2
        else:
            result = result*3 + 1
        answer += 1
    if (result != 1):
        answer = -1
    return answer