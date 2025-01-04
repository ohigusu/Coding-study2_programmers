def solution(n):
    answer = []
    for i in range(n):
        answer.append([0] * n)
    # 1~n까지 미리 이동한 것으로 처리
    answer[0] = list(range(1,n+1))
    # 좌우로 이동하는 횟수
    t_x = n
    # 상하로 이동하는 횟수
    t_y = n-1
    # 현재 좌표 x,y
    x, y = n-1, 0
    # answer[y][x] = (x,y) 에 들어갈 값 a 
    a = n
    while a < n**2: # 수를 다 채워서 a = n**2 라면 자동으로 종료
        # 아래로 이동 (y+=1)
        for i in range(t_y):
            a += 1
            y += 1
            answer[y][x] = a
        t_x -= 1

        # 왼쪽으로 이동 (x-=1)
        for i in range(t_x):
            a+=1
            x-=1
            answer[y][x] = a
        t_y -=1

        # 위로 이동 (y-=1)
        for i in range(t_y):
            a+=1
            y-=1
            answer[y][x]=a
        t_x-=1

        # 오른쪽으로 이동 (x+=1)
        for i in range(t_x):
            a+=1
            x+=1
            answer[y][x]=a
        t_y-=1

    return answer
