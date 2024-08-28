def solution(numbers, k):
    from collections import deque
    answer,i = 0,0
    numbers = deque(numbers)
    
    while True:
        i += 1
        if k == i :
            return numbers[0]
        numbers.append(numbers.popleft())
        numbers.append(numbers.popleft())
    return answer