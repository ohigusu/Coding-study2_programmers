def solution(word):
    answer = 0
    letters = ['A', 'E', 'I', 'O', 'U']

    def dfs(temp):
        nonlocal answer
        # 빈 문자열("")은 사전에 없으니, 길이가 1 이상일 때만 카운트
        if temp:
            answer += 1
            # 방금 센 단어가 목표라면 즉시 True를 리턴해 전체 탐색 중단
            if temp == word:
                return True

        # 길이 5에 도달하면 더 이상 확장하지 않음
        if len(temp) == 5:
            return False

        # A→E→I→O→U 순서로 재귀 탐색
        for c in letters:
            if dfs(temp + c):
                return True

        return False

    dfs("")  
    return answer
