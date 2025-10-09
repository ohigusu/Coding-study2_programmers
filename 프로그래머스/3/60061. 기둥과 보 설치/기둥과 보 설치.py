def solution(n, build_frame):
    S = set()  # {(x, y, a)}  a: 0=기둥, 1=보

    def can_place_pillar(x, y):
        # 기둥: 바닥 / 아래 기둥 / 현재 위치의 보 / 왼쪽 끝 보
        return (
            y == 0 or
            (x, y-1, 0) in S or
            (x-1, y, 1) in S or
            (x, y, 1) in S
        )

    def can_place_beam(x, y):
        # 보: 왼쪽 아래 기둥 / 오른쪽 아래 기둥 / 양쪽이 보로 연결
        return (
            (x, y-1, 0) in S or
            (x+1, y-1, 0) in S or
            ((x-1, y, 1) in S and (x+1, y, 1) in S)
        )

    def is_valid():
        # 현재 모든 부재가 규칙을 만족하는지 전체 점검
        for x, y, a in S:
            if a == 0 and not can_place_pillar(x, y):
                return False
            if a == 1 and not can_place_beam(x, y):
                return False
        return True

    for x, y, a, b in build_frame:
        if b == 1:            # 설치
            S.add((x, y, a))
            if not is_valid():
                S.remove((x, y, a))  # 롤백
        else:                  # 삭제
            if (x, y, a) in S:
                S.remove((x, y, a))
                if not is_valid():
                    S.add((x, y, a))  # 롤백

    return sorted(map(list, S), key=lambda t: (t[0], t[1], t[2]))