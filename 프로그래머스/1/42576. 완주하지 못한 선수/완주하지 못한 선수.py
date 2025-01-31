from collections import Counter
def solution(participant, completion):
    count = Counter(participant)  
    for name in completion:
        count[name] -= 1  
    for name, cnt in count.items():
        if cnt > 0:
            return name