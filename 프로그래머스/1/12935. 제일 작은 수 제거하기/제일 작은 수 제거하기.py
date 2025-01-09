def solution(arr):
    answer = []
    if len(arr) == 1 or not arr:
        return [-1]
    idx = arr.index(min(arr))
    answer=arr[:idx]+arr[idx+1:]
    return answer