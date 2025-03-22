def solution(word):
    answer = 0
    lis = ['A', 'E', 'I', 'O', 'U']
    found = False
    def dfs(temp):
        nonlocal answer, found
        if temp == word:
            found = True
            return 
        if len(temp) == 5:
            return
        for cha in lis:
            if found:
                return
            answer += 1
            dfs(temp+cha)
            
    dfs('')
    return answer