def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i < j:
                answer.append(numbers[i]*numbers[j])
    return max(answer)