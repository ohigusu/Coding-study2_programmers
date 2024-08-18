def solution(money):
    answer,i = [],0
    if money < 5500:
        return [0,money]
    while 1:
        money = money-5500
        i += 1
        if money < 5500:
            answer.append(i)
            answer.append(money)
            break
    return answer
    
#sol2
def solution(money):
    cup = money//5500
    change = money%5500
    return [cup, change]
