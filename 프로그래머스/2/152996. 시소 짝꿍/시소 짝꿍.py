from collections import Counter

def solution(weights):
    # 각 거리 쌍에 대응하는 (무게1 : 무게2) 비율 (d₂/d₁)
    # (d₁, d₂) ∈ {(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2),(4,3),(4,4)}
    # 이 중 d₁≠d₂는 3가지: (2↔3),(2↔4),(3↔4) → 비율 3/2, 4/2, 4/3
    ratios = [(1,1), (3,2), (4,2), (4,3)]
    
    freq = Counter(weights)
    total_pairs = 0
    
    # 1) 같은 몸무게끼리: freq[w]명 중 2명을 뽑는 조합
    for w, c in freq.items():
        total_pairs += c * (c - 1) // 2
    
    # 2) 서로 다른 몸무게끼리: w * (p/q) = w2 일 때
    #    w < w2 조건으로 중복 카운트 방지
    for w, c in freq.items():
        for p, q in ratios:
            # (1,1)은 동일 몸무게 경우이므로 스킵
            if (p, q) == (1, 1):
                continue
            # w * p가 q로 나누어떨어져야 w2가 정수
            if (w * p) % q != 0:
                continue
            w2 = (w * p) // q
            if w < w2 and w2 in freq:
                total_pairs += c * freq[w2]
    
    return total_pairs
