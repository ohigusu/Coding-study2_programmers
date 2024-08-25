def solution(numbers, direction):
    answer,n = [],len(numbers)
    if direction == "right":
        answer.append(numbers[n-1])
        for i in range(0,n-1):
            answer.append(numbers[i])
    else:
        for i in range(1,n):
            answer.append(numbers[i])
        answer.append(numbers[0]) 
    return answer