from collections import Counter
def solution(k, tangerine):
    answer = 0
    total = 0
    li = Counter(tangerine)
    li_sort=sorted(li.items(),key=lambda x: x[1],reverse=True)
    for kind,cnt in li_sort:
        if total >= k:
            break
        else:
            total += cnt
            answer += 1           
    return answer