def solution(age):
    answer = ''
    age_1 = [str(i) for i in range(10)]
    age_2 = [chr(i) for i in range(97, 108)]
    encode = dict(zip(age_1, age_2))
    for i in str(age):
        answer+=encode[i]
    return answer