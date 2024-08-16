from collections import Counter

def solution(array):
    # 배열에서 각 요소의 빈도수를 셈
    counter = Counter(array)
  
    # 가장 빈도수가 높은 값을 찾음
    max_count = max(counter.values())
    # 최빈값 후보들을 리스트로 만듦
    modes = [key for key, count in counter.items() if count == max_count]
    
    # 최빈값이 여러 개라면 -1 반환
    if len(modes) > 1: return -1
    # 그렇지 않으면 최빈값 반환
    return modes[0]
