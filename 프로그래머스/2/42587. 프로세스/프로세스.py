from collections import deque
def solution(priorities, location):
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    answer = 0
    while queue:
        now = queue.popleft()
        if any(now[0] < other[0] for other in queue):
            queue.append(now)
        else:
            answer += 1
            if now[1] == location:
                return answer
