def solution(babbling):
    li = ["aya","ye","woo","ma"]
    answer= 0
    for bab in babbling:
        pre_i,ans,pre_ans  = -1,'',''
        for i in range(0,len(bab)-1):
            for j in range(i+1,len(bab)):
                if i <= pre_i:
                    continue
                elif bab[i:j+1] in li and bab[i:j+1] != pre_ans:
                    pre_i = i 
                    pre_ans = bab[i:j+1]
                    ans += bab[i:j+1]
        if len(ans) == len(bab):
            answer += 1
    return answer