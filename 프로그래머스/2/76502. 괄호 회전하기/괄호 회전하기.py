def solution(s):
    answer = 0
    for i in range(len(s)):
        new_s = s[i:] + s[:i]
        stack = []
        valid = True
        for j in new_s:
            if j in "([{":
                stack.append(j)
            else:
                if not stack:
                    valid=False
                    break
                now=stack.pop()
                if now!="(" and j == ")":
                    valid=False
                    break
                elif now!="[" and j =="]":
                    valid=False
                    break
                elif now!="{" and j=="}":
                    valid=False
                    break
        if valid and not stack:
            answer += 1   
    return answer