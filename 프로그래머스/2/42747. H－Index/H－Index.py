def solution(citations):
    n = len(citations)
    answer = n
    citations_sort = sorted(citations,reverse=True) #내림차순
    for i, cite in enumerate(citations_sort):
        if cite <= i:
            return i
    return len(citations)