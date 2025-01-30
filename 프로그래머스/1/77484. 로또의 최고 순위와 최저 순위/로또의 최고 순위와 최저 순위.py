def solution(lottos, win_nums):
    correct = sum(1 for num in lottos if num in win_nums)  
    non_know = lottos.count(0)
    return [min(7 - (correct + non_know), 6), min(7 - correct, 6)]