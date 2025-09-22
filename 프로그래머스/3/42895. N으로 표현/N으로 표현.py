def solution(N, number):
    if N == number:
        return 1

    dp = [set() for _ in range(9)]  # 1..8 사용, dp[0]은 비움

    for i in range(1, 9):
        # 1) 붙여쓰기(예: 5, 55, 555, ...)
        dp[i].add(int(str(N) * i))

        # 2) 분할 결합: i = j + (i-j)
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i - j]:
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
                    if b != 0:
                        dp[i].add(a // b)  # 정수 나눗셈

        if number in dp[i]:
            return i

    return -1