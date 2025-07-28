import heapq
def solution(n, works):
    # 야근 피로도 = SUM(야근을 시작한 시점에서 남은 일의 작업량 ^ 2)
    # 각 일에 대한 작업량 works에 대해 야근 피로도를 최소화한 값
    answer = 0
    if sum(works) <= n:
        return 0
    works = [-w for w in works]
    heapq.heapify(works)
    while n > 0:
        a = heapq.heappop(works)
        heapq.heappush(works, a+1)
        n -= 1
        
    for i in works:
        answer += i**2
    return answer