#sol1
def solution(array, n):
    answer = 0 
    for i in array:
        if i == n:
            answer += 1
    return answer
#sol2
def solution(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]
