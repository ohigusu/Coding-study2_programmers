def is_parallel(a, b, c, d):
    x, y = 0, 1
    g1 = (b[y] - a[y]) / (b[x] - a[x])
    g2 = (d[y] - c[y]) / (d[x] - c[x])

    return 1 if g1 == g2 else 0


def solution(dots):
    dots.sort(key=lambda x: x[0])
    answer = 0
    a, b, c, d = dots

    aa = is_parallel(a, b, c, d)
    bb = is_parallel(a, c, b, d)
    cc = is_parallel(a, d, b, c)

    if 1 in [aa, bb, cc]:
        answer = 1

    return answer