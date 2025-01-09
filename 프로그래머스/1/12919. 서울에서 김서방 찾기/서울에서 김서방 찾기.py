def solution(seoul):
    answer = '김서방은 '
    for idx,name in enumerate(seoul):
        if name == "Kim":
            answer += (str(idx)+"에 있다")
            break
    return answer