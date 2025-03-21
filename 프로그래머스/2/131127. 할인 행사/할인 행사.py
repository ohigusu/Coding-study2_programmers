from collections import Counter
def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-10+1):
        li_discount = Counter(discount[i:i+10])
        conti = True
        for name, num in zip(want,number):
            if name not in li_discount or num > li_discount[name]:
                conti = False
                break
        if conti:
            answer += 1
    return answer