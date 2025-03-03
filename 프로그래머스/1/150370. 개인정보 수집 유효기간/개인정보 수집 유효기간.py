def solution(today, terms, privacies):
    '''
    오늘 날짜를 의미하는 문자열 today
    약관의 유효기간을 담은 1차원 문자열 배열 terms
    수집된 개인정보의 정보를 담은 1차원 문자열 배열 privacies
    return:
    파기해야 할 개인정보의 번호를 오름차순으로
    '''
    answer = []
    rec = {}
    t_y,t_m,t_d = map(int,today.split("."))
    for term in terms:
        rec[term.split()[0]] = int(term.split()[1])
    for idx,privacy in enumerate(privacies):
        dat = privacy.split()[1]
        n = rec[dat]
        y,m,d = map(int,privacy.split()[0].split("."))
        
        end_y = y + (m + n - 1) // 12
        end_m = (m + n - 1) % 12 + 1
        end_d = (d - 1 + 27) % 28 + 1
        if end_d == 28:
            end_m = (end_m - 1 + 11) % 12 + 1
            if end_m == 12:
                end_y -= 1
        
        if (t_y > end_y) or (t_y == end_y and t_m > end_m) or (t_y == end_y and t_m == end_m and t_d > end_d):
            answer.append(idx + 1)
    return answer