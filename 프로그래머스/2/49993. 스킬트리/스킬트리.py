def solution(skill, skill_trees):
    answer = 0
    n = len(skill)
    
    for skill_tree in skill_trees:
        m = len(skill_tree)
        pre_j = m+1
        con,pl =True,True
        cnt = 0
        for idx in range(n-1,-1,-1):
            if skill[idx] in skill_tree and con:
                for j in range(0,m):
                    if skill[idx] == skill_tree[j]:
                        if pre_j < j:
                            con,pl = False,False
                            break
                        else:
                            pre_j = j
                            cnt += 1
            if skill[idx] not in skill_tree:
                if cnt > 0:
                    pl = False
            if not con:
                break
        if pl:
            answer += 1   
    return answer