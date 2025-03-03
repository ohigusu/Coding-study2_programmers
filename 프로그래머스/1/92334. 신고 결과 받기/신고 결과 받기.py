def solution(id_list, report, k):
    '''
    이용자의 ID:id_list
    각 이용자가 신고한 이용자의 ID 정보:report
    정지 기준이 되는 신고 횟수:k
    return
    각 유저별로 처리 결과 메일을 받은 횟수
    '''
    n = len(id_list)
    answer = [0]*n
    result = [[0]*n for _ in range(n+1)]
    for rep in set(report):
        give, receive = rep.split(" ")
        give_idx,receive_idx = id_list.index(give),id_list.index(receive)
        result[give_idx][receive_idx] = 1
        result[n][receive_idx] += 1
    for idx,i in enumerate(result[n]):
        if i < k:
            pass
        else:
            for j in range(n):
                if result[j][idx]:
                    answer[j] += 1
    return answer
    