from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])
    visited = [False]*len(words)
    
    while queue:
        now_word,steps = queue.popleft()
        if now_word == target:
            return steps
        n = len(now_word)
        for i in range(n):
            if i == 0:
                front,back = now_word[i],now_word[i+1:]
                for idx,word in enumerate(words):
                    f,b = word[i],word[i+1:]
                    if front != f and back == b and not visited[idx]:
                        queue.append((word,steps+1))
                        visited[idx]=True
            elif i == n-1:
                front,back=now_word[:i],now_word[i]
                for idx,word in enumerate(words):
                    f,b = word[:i],word[i]
                    if front == f and back != b and not visited[idx]:
                        queue.append((word,steps+1))
                        visited[idx]=True
                        
            else:
                front,cha, back = now_word[:i],now_word[i],now_word[i+1:]
                for idx,word in enumerate(words):
                    f,c,b = word[:i],word[i],word[i+1:]
                    if front == f and back == b and cha != c and not visited[idx]:
                        queue.append((word,steps+1))
                        visited[idx]=True
    return answer