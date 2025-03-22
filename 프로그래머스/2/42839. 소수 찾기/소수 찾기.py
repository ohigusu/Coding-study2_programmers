def solution(numbers):
    answer = 0
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def dfs(temp,storage):
        nonlocal answer
        if temp != "":
            num = int(temp)
            if num not in storage:
                storage.add(num)
                if is_prime(num):
                    answer += 1    
        for i in numbers:
            if temp.count(i) < numbers.count(i):
                dfs(temp+i,storage)
    dfs("",set())
    return answer