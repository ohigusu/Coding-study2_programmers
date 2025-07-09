import heapq

def solution(book_time):

    def to_minutes(t):
        h, m = map(int, t.split(":"))
        return h * 60 + m

    intervals = []
    for start, end in book_time:
        s = to_minutes(start)
        e = to_minutes(end) + 10  
        intervals.append((s, e))
    
    # 시작 시간 기준 오름차순
    intervals.sort(key=lambda x: x[0])

    heap = []
    
    for s, e in intervals:
        if heap and heap[0] <= s:
            heapq.heappop(heap)
        heapq.heappush(heap, e)
    
    return len(heap)