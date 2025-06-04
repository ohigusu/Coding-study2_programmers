def solution(order):
    answer,idx = 0,0
    n = len(order)
    stack = []
    for i in range(1,n+1):
        if i == order[idx]:
            idx += 1
            answer += 1
            while stack and stack[-1]==order[idx]:
                stack.pop()
                idx += 1
                answer += 1
        else:
            stack.append(i)
    while stack and idx<n and stack[-1]==order[idx]:
        stack.pop()
        answer+=1
        idx+=1
    return answer