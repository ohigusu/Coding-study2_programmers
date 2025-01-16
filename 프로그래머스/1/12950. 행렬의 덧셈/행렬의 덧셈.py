def solution(arr1, arr2):
    answer = []
    for a,b in zip(arr1,arr2):
        result = []
        for i,j in zip(a,b):
            result.append(i+j)
        answer.append(result)
    return answer