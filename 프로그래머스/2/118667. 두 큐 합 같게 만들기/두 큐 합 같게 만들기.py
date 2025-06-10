from collections import deque
from collections import deque
def solution(queue1, queue2):
    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    for i in range(4 * len(queue1) + 1):
        if queue1_sum > queue2_sum:
            x = queue1.popleft()
            queue1_sum -= x
            queue2_sum += x
            queue2.append(x)
        elif queue1_sum < queue2_sum:
            x = queue2.popleft()
            queue2_sum -= x
            queue1_sum += x
            queue1.append(x)
        else:
            return i
    return -1
