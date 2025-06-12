def solution(arr):
    answer = [0, 0]

    def compress(x, y, size):
        initial = arr[x][y]
        all_same = True

        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != initial:
                    all_same = False
                    break
            if not all_same:
                break
        if all_same:
            answer[initial] += 1
        else:
            half = size // 2
            if half > 0:
                compress(x, y, half)
                compress(x, y + half, half)
                compress(x + half, y, half)
                compress(x + half, y + half, half)

    compress(0, 0, len(arr))
    return answer