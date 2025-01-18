def solution(d, budget):
    d.sort()
    for idx,cost in enumerate(d):
        budget -= d[idx]
        if budget < 0:
            return idx  
    return len(d)