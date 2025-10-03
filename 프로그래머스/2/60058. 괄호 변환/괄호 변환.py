def solution(p):
    from collections import deque
    def isbalance(words):
        l_cnt,r_cnt = 0,0
        for word in words:
            if word == "(":
                l_cnt += 1
            else: 
                r_cnt += 1
        return l_cnt == r_cnt
    def isalright(words):
        stack=[]
        for ch in words:
            if ch == "(":
                stack.append(ch)
            else:
                if not stack:
                    return False
                stack.pop()
        return not stack
    
    def cnt(s):
        l_cnt,r_cnt = 0,0
        for idx,value in enumerate(s):
            if value == "(":
                l_cnt += 1
            else:
                r_cnt += 1
            if l_cnt == r_cnt:
                u,v = s[:idx+1],s[idx+1:]
                return u,v
        return s,""
    
    def last(p):
        answer = ''
        if p=='':
            return answer
        
        if isbalance(p):
            u,v = cnt(p)
            if isalright(u):
                return u + last(v)
            else:
                answer = "("
                answer += last(v)
                answer += ")"
                u = list(u[1:-1])
                for i in range(len(u)):
                    if u[i] =="(":
                        u[i] = ")"
                    else:
                        u[i] = "("
                answer += "".join(u)
        return answer
    
    return last(p)