import math
def solution(n):
    answer = 0
    for two_num in range(n // 2 + 1):
        one_num = n - 2 * two_num
        answer += math.comb(two_num+one_num,one_num) 
    return answer% 1234567