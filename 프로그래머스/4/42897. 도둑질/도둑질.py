def solution(money):
    n = len(money)
    if n == 1:
        return money[0]
    if n == 2:
        return max(money[0], money[1])

    def rob_linear(arr):
        # 선형 배열에서 인접 집을 동시에 못 털 때의 최대 금액
        prev2, prev1 = 0, 0  # dp[i-2], dp[i-1]
        for x in arr:
            prev2, prev1 = prev1, max(prev1, prev2 + x)
        return prev1

    # 원형이라 첫 집과 마지막 집을 함께 못 고름 → 두 케이스로 분할
    case1 = rob_linear(money[1:])   # 첫 집 제외
    case2 = rob_linear(money[:-1])  # 마지막 집 제외
    return max(case1, case2)