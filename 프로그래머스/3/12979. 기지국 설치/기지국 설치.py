import math
def solution(n, stations, w):
    cover = 2*w+ 1  # 새로 세우는 5G 기지국 1대가 덮는 연속 길이
    answer = 0
    prev_covered_end = 0  # 직전까지 전파가 닿은 마지막 아파트 번호 (초기 0: 아직 아무 것도 안 덮음)

    for s in stations:
        left = max(1, s - w)
        right = min(n, s + w)

        # 앞쪽 빈 구간: (prev_covered_end+1) ~ (left-1)
        gap_len = left - prev_covered_end - 1
        if gap_len > 0:
            answer += math.ceil(gap_len / cover)

        # 현재 기지국까지 커버 반영
        prev_covered_end = right

        # 조기 종료 최적화(선택): 이미 끝까지 덮었으면 더 볼 필요 없음
        if prev_covered_end >= n:
            return answer

    # 마지막 기지국 이후의 꼬리 빈 구간 처리: (prev_covered_end+1) ~ N
    tail_len = n - prev_covered_end
    if tail_len > 0:
        answer += math.ceil(tail_len / cover)

    return answer