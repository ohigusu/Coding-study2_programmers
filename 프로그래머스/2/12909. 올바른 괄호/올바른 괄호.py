def solution(s):
    ans = []
    for i in s:
        if i == "(":
            ans.append(i)
        else:
            if not ans: 
                return False
            ans.pop()
    return len(ans) == 0