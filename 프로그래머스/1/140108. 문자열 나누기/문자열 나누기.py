def solution(s):
    answer = 0  # 분해된 문자열 개수
    count_x, count_other = 0, 0  # 첫 글자의 개수와 다른 글자의 개수
    first_char = None  # 현재 구간에서 첫 번째 등장한 문자

    for char in s:
        if first_char is None:
            first_char = char  # 첫 문자 설정
        if char == first_char:
            count_x += 1
        else:
            count_other += 1

        # x의 개수와 다른 글자의 개수가 같아지면 분리
        if count_x == count_other:
            answer += 1
            first_char = None  # 새로운 구간 시작
            count_x, count_other = 0, 0  # 카운트 초기화

    # 마지막 남은 문자열이 있다면 하나의 구간으로 추가
    if count_x != count_other:
        answer += 1

    return answer