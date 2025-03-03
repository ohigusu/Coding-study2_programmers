def solution(park, routes):
    H, W = len(park), len(park[0])
    for r in range(H):
        for c in range(W):
            if park[r][c] == 'S':
                pre_r, pre_c = r, c
    direction = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}
    for route in routes:
        op, n = route.split()
        n = int(n)
        dr, dc = direction[op]
        
        new_r, new_c = pre_r, pre_c
        valid_move = True
        
        
        for _ in range(n):
            new_r += dr
            new_c += dc
            # 경계를 벗어나거나 장애물(X)을 만나면 이동 불가
            if not (0 <= new_r < H and 0 <= new_c < W) or park[new_r][new_c] == 'X':
                valid_move = False
                break

        # 이동 가능하면 위치 업데이트
        if valid_move:
            pre_r, pre_c = new_r, new_c
    return [pre_r, pre_c]