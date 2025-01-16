def solution(arr):
    answer = []
    temp = None
    for num in arr:
        if num != temp:
            answer.append(num)
            temp = num
    return answer