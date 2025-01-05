def solution(a, b, c, d):
    # 주사위 결과를 리스트로 변환하고 카운트 계산
    dice = [a, b, c, d]
    counts = {x: dice.count(x) for x in set(dice)}

    # 모든 숫자가 같을 때
    if len(counts) == 1:
        p = a  # 모든 숫자가 같으므로 p는 어느 숫자나 상관없음
        return 1111 * p

    # 세 숫자가 같고, 나머지 하나가 다를 때
    if len(counts) == 2:
        # p가 3번, q가 1번 등장하는 경우 탐색
        p, q = None, None
        for num, count in counts.items():
            if count == 3:
                p = num
            elif count == 1:
                q = num
        if p is not None and q is not None:
            return (10 * p + q) ** 2

        # 두 숫자가 각각 두 번씩 등장하는 경우
        if all(value == 2 for value in counts.values()):
            p, q = list(counts.keys())
            return (p + q) * abs(p - q)

    # 두 숫자가 같고, 나머지 두 숫자가 각각 다를 때
    if len(counts) == 3:
        # p가 2번 등장하고, q와 r이 각각 1번 등장하는 경우 탐색
        p, q, r = None, None, None
        for num, count in counts.items():
            if count == 2:
                p = num
            elif count == 1:
                if q is None:
                    q = num
                else:
                    r = num
        if p is not None and q is not None and r is not None:
            return q * r

    # 모든 숫자가 다를 때
    if len(counts) == 4:
        return min(dice)
