T = int(input())  # 테스트 케이스 수

for _ in range(T):
    n = int(input())  # 열의 수 (스티커 개수)

    top = list(map(int, input().split()))
    bottom = list(map(int, input().split()))

    if n == 1:
        print(max(top[0], bottom[0]))
        continue

    # DP 테이블 초기화
    dp_top = [0] * n
    dp_bottom = [0] * n

    # 초기값 설정
    dp_top[0] = top[0]
    dp_bottom[0] = bottom[0]
    dp_top[1] = bottom[0] + top[1]
    dp_bottom[1] = top[0] + bottom[1]

    # 점화식 적용
    for i in range(2, n):
        dp_top[i] = max(dp_bottom[i-1], dp_bottom[i-2]) + top[i]
        dp_bottom[i] = max(dp_top[i-1], dp_top[i-2]) + bottom[i]

    # 마지막 열의 최댓값 출력
    print(max(dp_top[n-1], dp_bottom[n-1]))
