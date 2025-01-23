def solution(a, b):
    name = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    month_day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    days = 0
    for month in range(0, a):
        days += month_day[month]
    answer = name[(days + b) % 7]
    return answer