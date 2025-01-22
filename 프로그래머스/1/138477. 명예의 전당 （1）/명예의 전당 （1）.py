def solution(k, score):
    '''
    입력:
        k : 명예의 전당 목록의 점수의 개수
        score : 1일부터 마지막 날까지 출연한 가수들의 점수
    출력:
        매일 발표된 명예의 전당의 최하위 점수
    '''
    answer = []
    for i in range(len(score)):
        if i < k:
            store = score[:i+1]
            answer.append(min(store))
            continue
        else:
            store.append(score[i])
            store.sort(reverse=True)
            answer.append(store[k-1])
    return answer