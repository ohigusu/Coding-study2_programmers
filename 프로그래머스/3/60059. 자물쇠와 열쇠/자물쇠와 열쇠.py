def solution(key, lock):
    # 시계 방향 90도 회전
    def rotate_a_matrix_by_90(a):
        n, m = len(a), len(a[0])
        result = [[0]*n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                result[j][n - i - 1] = a[i][j]
        return result

    # 중앙 N×N 영역이 모두 1인지 확인
    def check(new_lock):
        lock_length = len(new_lock) // 3
        for i in range(lock_length, lock_length * 2):
            for j in range(lock_length, lock_length * 2):
                if new_lock[i][j] != 1:
                    return False
        return True

    n, m = len(lock), len(key)

    # 3배 확장한 보드에 자물쇠를 가운데 배치
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j]

    # 4회전 × 모든 위치 시도
    for _ in range(4):
        key = rotate_a_matrix_by_90(key)  # 회전
        for x in range(n * 2 + 1):
            for y in range(n * 2 + 1):
                # 키 더하기(오버레이)
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                if check(new_lock):
                    return True

                # 롤백(되돌리기)
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return False

