from collections import deque

DIRS = [(-1,0),(1,0),(0,1),(0,-1)]

def bfs_collect(board, r, c, target):
    """board에서 (r,c)부터 target(0/1)과 연결된 좌표들을 모아 반환.
       시작 칸이 target이 아니면 빈 리스트 반환."""
    n = len(board)
    if board[r][c] != target:
        return []
    q = deque([(r, c)])
    board[r][c] = 1 - target  # 방문표시(값 뒤집기)
    coords = [(r, c)]
    while q:
        x, y = q.popleft()
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == target:
                board[nx][ny] = 1 - target
                q.append((nx, ny))
                coords.append((nx, ny))
    return coords  # [(r,c), ...]

def normalize(coords):
    """좌상단(0,0)으로 평행이동 + 정렬 → 튜플의 튜플로 반환(해시 가능)."""
    min_r = min(r for r, _ in coords)
    min_c = min(c for _, c in coords)
    shape = tuple(sorted((r - min_r, c - min_c) for r, c in coords))
    return shape  # ((r,c), ...)

def rotate(shape):
    """정규화된 shape를 시계 90° 회전하고 다시 정규화해서 반환."""
    # shape는 ((r,c), ...) 형태(튜플). 바운딩박스 높이 H 사용.
    H = max(r for r, _ in shape) + 1
    rotated = [(c, H - 1 - r) for r, c in shape]
    return normalize(rotated)  # 항상 회전 후 정규화!

def all_rotations(shape):
    """0/90/180/270° 회전한 모양들의 집합(중복 제거). 전부 튜플."""
    s0 = shape
    s1 = rotate(s0)
    s2 = rotate(s1)
    s3 = rotate(s2)
    return {s0, s1, s2, s3}  # set of tuple

def solution(game_board, table):
    n = len(game_board)

    # 1) game_board에서 '구멍'(0 묶음) 추출
    gb = [row[:] for row in game_board]
    holes = []
    for i in range(n):
        for j in range(n):
            if gb[i][j] == 0:
                coords = bfs_collect(gb, i, j, target=0)
                if coords:
                    holes.append(normalize(coords))

    # 2) table에서 '블록'(1 묶음) 추출
    tb = [row[:] for row in table]
    blocks = []
    for i in range(n):
        for j in range(n):
            if tb[i][j] == 1:                 # <-- 반드시 체크!
                coords = bfs_collect(tb, i, j, target=1)
                if coords:
                    blocks.append(normalize(coords))

    # 3) 블록의 4회전 모양 set 준비
    used = [False] * len(blocks)
    rotated_sets = [all_rotations(b) for b in blocks]  # 각 원소는 set of tuple

    # 4) 구멍마다 아직 안 쓴 블록과 매칭
    answer = 0
    for hole in holes:
        for idx, rset in enumerate(rotated_sets):
            if used[idx]:
                continue
            if hole in rset:
                used[idx] = True
                answer += len(hole)
                break
    return answer
