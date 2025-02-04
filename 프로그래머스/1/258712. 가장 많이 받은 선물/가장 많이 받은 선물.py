from collections import Counter

def solution(friends, gifts):
    n = len(friends)
    
    # 친구 이름을 인덱스로 변환하는 딕셔너리
    friend_idx = {name: i for i, name in enumerate(friends)}
    
    # 선물 주고받은 횟수 저장할 행렬
    matrix = [[0] * n for _ in range(n)]
    
    # 준 선물, 받은 선물, 선물 지수
    give = [0] * n
    receive = [0] * n
    indicator = [0] * n
    result = [0] * n  # 다음 달 받을 선물 수
    
    # 선물 기록 저장 (matrix 업데이트)
    for gift in gifts:
        giver, receiver = gift.split()
        g_idx = friend_idx[giver]
        r_idx = friend_idx[receiver]
        matrix[g_idx][r_idx] += 1

    # 각 친구별 준 선물과 받은 선물 계산
    for i in range(n):
        for j in range(n):
            give[i] += matrix[i][j]  # i가 준 선물 수
            receive[i] += matrix[j][i]  # i가 받은 선물 수
    
    # 선물 지수 계산
    for i in range(n):
        indicator[i] = give[i] - receive[i]

    # 다음 달 선물 계산
    for i in range(n):
        for j in range(i + 1, n):  # (i, j) 쌍만 확인하여 중복 검사 방지
            if matrix[i][j] > matrix[j][i]:  # i → j에게 더 많이 줬으면 i가 받음
                result[i] += 1
            elif matrix[i][j] < matrix[j][i]:  # j → i에게 더 많이 줬으면 j가 받음
                result[j] += 1
            else:  # 주고받은 수가 같다면 선물 지수 비교
                if indicator[i] > indicator[j]:  
                    result[i] += 1
                elif indicator[i] < indicator[j]:  
                    result[j] += 1

    return max(result)  # 가장 많이 받는 사람의 선물 수 반환
