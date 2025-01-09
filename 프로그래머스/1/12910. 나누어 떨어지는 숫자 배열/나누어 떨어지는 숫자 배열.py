def solution(arr, divisor):
    answer = [ i for i in arr if i%divisor == 0]
    answer.sort()
    return answer if len(answer) != 0 else [-1]