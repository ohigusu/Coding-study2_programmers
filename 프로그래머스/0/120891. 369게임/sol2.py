#string1
def solution(order):
    order = str(order)
    return order.count('3') + order.count('6') + order.count('9')

#string2
def solution(order):
    answer = len([1 for char in str(order) if char in "369"])
    return answer
