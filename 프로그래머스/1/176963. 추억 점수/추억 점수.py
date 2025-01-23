def solution(name, yearning, photo):
    '''
    입력: 
        name:그리워하는 사람의 이름을 담은 문자열 배열
        yearning:각 사람별 그리움 점수를 담은 정수 배열
        photo: 각 사진에 찍힌 인물의 이름을 담은 이차원 문자열 배열
    출력:
        사진들의 추억 점수
    '''
    answer = []
    for pho in photo:
        ans = 0
        for i in pho:
            if i in name:
                idx = name.index(i)
                ans += yearning[idx]
        answer.append(ans) 
    return answer