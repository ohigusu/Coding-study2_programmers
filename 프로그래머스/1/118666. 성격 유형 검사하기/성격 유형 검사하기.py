def solution(survey, choices):
    answer = ''
    result = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for i,j in zip(survey,choices):
        if j > 4:
            result[i[1]] += j-4
        else:
            result[i[0]] += 4-j
    answer += 'R' if result['R'] >= result['T'] else 'T'
    answer += 'C' if result['C'] >= result['F'] else 'F'
    answer += 'J' if result['J'] >= result['M'] else 'M'
    answer += 'A' if result['A'] >= result['N'] else 'N'
    return answer

