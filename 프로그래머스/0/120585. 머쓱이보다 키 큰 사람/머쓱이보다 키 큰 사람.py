def solution(array, height):
    answer = []
    array.sort()
    for i in range(len(array)):
        if array[i] > height:
            answer.append(i)
    return len(answer)