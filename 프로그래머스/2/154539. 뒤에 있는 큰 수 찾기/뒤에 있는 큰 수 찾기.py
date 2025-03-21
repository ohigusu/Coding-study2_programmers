def solution(numbers):
    n = len(numbers)
    answer = [-1] * n  # 결과 배열 초기화
    stack = []  # 뒤에서부터 큰 수 후보를 담는 스택

    for i in range(n - 1, -1, -1):  # 오른쪽 → 왼쪽으로 탐색
        # 스택에서 현재 수보다 작거나 같은 수는 제거
        while stack and stack[-1] <= numbers[i]:
            stack.pop()

        # 스택이 비어있지 않으면, top이 뒷 큰수
        if stack:
            answer[i] = stack[-1]

        # 현재 값을 스택에 push
        stack.append(numbers[i])

    return answer
