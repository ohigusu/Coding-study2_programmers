def solution(x, n):
    answer = []
    diff = x
    for _ in range(n):
        answer.append(x)
        x += diff
    return answer