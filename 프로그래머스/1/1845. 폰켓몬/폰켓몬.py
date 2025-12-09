def solution(nums):
    N = len(nums)
    goal = N//2
    set_n = len(set(nums))
    if set_n < goal:
        return set_n
    else:
        return goal
        
    