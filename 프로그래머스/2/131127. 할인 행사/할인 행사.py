from collections import Counter
def solution(want, number, discount):
    answer = 0
    dic_want = dict(zip(want,number))
    for i in range(len(discount)-10+1):
        li_discount = Counter(discount[i:i+10])
        if dic_want == li_discount:
                answer += 1
    return answer