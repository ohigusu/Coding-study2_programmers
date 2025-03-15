def solution(n):
    ans = 0  
    #5 = 0->1,2,4->5
    #6 = 0->1,2->3,6
    #5000 = 0->1,2,4,8->9,18->19,38->39,78,156,312,624->625,1250,2500
    while n > 0:
        if n%2 == 1:#odd number
            ans += 1
            n -= 1
        else:
            n = n//2     
    return ans