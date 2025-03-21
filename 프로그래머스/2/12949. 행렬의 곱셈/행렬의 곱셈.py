def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        row = arr1[i]
        s = []
        for j in range(len(arr2[1])):
            k = 0
            sum_c = 0
            while k < len(arr2):
                sum_c += row[k]*arr2[k][j]
                k += 1
            s.append(sum_c)
            
        answer.append(s)
    return answer
