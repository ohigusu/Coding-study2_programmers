from collections import defaultdict

def solution(tickets):
    routes = defaultdict(list)
    for a,b in tickets:
        routes[a].append(b)
    for a in routes:
        routes[a].sort(reverse=True)
        
    path = []
    stack = ["ICN"]

    while stack:
        start = stack[-1]
        if routes[start]:
            stack.append(routes[start].pop())
        else:
            path.append(stack.pop())
    return path[::-1]