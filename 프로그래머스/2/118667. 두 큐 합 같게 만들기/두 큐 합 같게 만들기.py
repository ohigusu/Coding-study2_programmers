from collections import deque

def solution(queue1, queue2):
    dq1 = deque(queue1)
    dq2 = deque(queue2)
    sum1 = sum(dq1)
    sum2 = sum(dq2)

    total = sum1 + sum2
    # 1) 전체 합이 홀수면 불가능
    if total % 2 != 0:
        return -1

    target = total // 2
    cnt = 0
    # 2) 안전한 최대 연산 횟수 (두 큐 길이의 3배 정도면 충분)
    max_ops = len(queue1) * 3

    # 3) pop + append 를 1회로 간주
    while cnt < max_ops:
        if sum1 == target:
            return cnt
        if sum1 < target:
            # queue2 -> queue1
            v = dq2.popleft()
            sum2 -= v
            dq1.append(v)
            sum1 += v
        else:
            # queue1 -> queue2
            v = dq1.popleft()
            sum1 -= v
            dq2.append(v)
            sum2 += v
        cnt += 1

    return -1
