def solution(price, money, count):
    answer = -1
    for i in range(1,count+1):
        money -= i*price
    return answer*money if money < 0 else 0