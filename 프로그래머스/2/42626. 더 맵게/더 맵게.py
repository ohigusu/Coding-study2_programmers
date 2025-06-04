import heapq

def solution(scoville,K):
    answer = 0
    heapq.heapify(scoville)
    while scoville:
        smallest = scoville[0]
        if smallest >= K:
            return answer
        if len(scoville) < 2:
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new_scoville = first + second * 2

        heapq.heappush(scoville, new_scoville)

        answer += 1    
    return -1