import heapq
def solution(operations):
    answer = []
    min_heap,max_heap = [],[]
    idx = 0
    visited = dict()
    for operation in operations:
        if operation[0] == "I":
            num = int(operation[2:])
            heapq.heappush(min_heap,(num,idx))
            heapq.heappush(max_heap,(-num,idx))
            visited[idx] = True
            idx += 1
        elif operation == "D 1":
            while max_heap and not visited[max_heap[0][1]]:
                heapq.heappop(max_heap)
            if max_heap:
                _,del_idx = heapq.heappop(max_heap)
                visited[del_idx] = False
        elif operation == "D -1":
            while min_heap and not visited[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                _,del_idx = heapq.heappop(min_heap)
                visited[del_idx]=False
        
        while min_heap and not visited[min_heap[0][1]]:
            heapq.heappop(min_heap)
        while max_heap and not visited[max_heap[0][1]]:
            heapq.heappop(max_heap)
            
    if not min_heap or not max_heap:
        return [0,0]
    else:
        return [-max_heap[0][0], min_heap[0][0]]
