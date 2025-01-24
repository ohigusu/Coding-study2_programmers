def solution(nums):
    '''
    홀수+홀수+짝수=짝수
    짝수+짝수+짝수=짝수 
    홀수+홀수+홀수=홀수, 홀수+짝수+짝수=홀수
    '''
    answer = 0
#     for i in range(0,len(nums)-2):
#         for j in range(i+1,len(nums)-1):
#             for k in range(j+1,len(nums)):
#                 su = nums[i]+nums[j]+nums[k]
#                 if su % 2 == 0:
#                     continue
                    
#                 tf = True
#                 for de in range(3,int(su**0.5)+1,2):
#                     if su%de==0:
#                         tf=False
#                         break
#                 if tf:
#                     answer += 1
    from itertools import combinations as comb
    for i in comb(nums,3):
        s = sum(i)
        if s%2 == 0:
            continue
        tf = True
        for de in range(3,int(s**0.5)+1):
            if s%de==0:
                tf = False
                break
        if tf:
            answer+=1
    return answer