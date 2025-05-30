import heapq

N = int(input())
course = [tuple(map(int, input().split())) for _ in range(N)]
course.sort()

heap = []
heapq.heappush(heap, course[0][1])

for i in range(1, N):
    s, t = course[i]

    if heap[0] <= s:
        heapq.heappop(heap)
    
    heapq.heappush(heap, t)

print(len(heap))