def solution(s):
    zero_cnt = 0
    cnt = 0
    while s != "1":
        zero_cnt += s.count('0')
        s = s.replace("0","")
        s = bin(len(s))[2:]         
        cnt += 1 
    return [cnt,zero_cnt]