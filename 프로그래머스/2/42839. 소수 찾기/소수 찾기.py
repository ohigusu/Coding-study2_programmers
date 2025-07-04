def solution(numbers):
    answer = 0
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    visited = [False]*len(numbers)
    def backtrack(path,store):
        nonlocal answer
        if len(path) > 0:
            num = int("".join(path))
            if num not in store:
                store.append(num)
                if is_prime(num):
                    answer += 1
        if len(path) == len(numbers):
            return
        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                path.append(numbers[i])
                backtrack(path,store)
                path.pop()
                visited[i]=False
    backtrack([],[])
    return answer