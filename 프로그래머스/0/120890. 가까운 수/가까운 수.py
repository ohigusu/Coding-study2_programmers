def solution(array, n):
    array.sort()
    if n <= array[0]: 
        return array[0]
    elif n >= array[len(array)-1]: 
        return array[len(array)-1]

    T,start,end = True,0,len(array)-1
    while T:
        mid = ((end-start)//2) + start 
        if array[mid] < n:
            start,end = mid,end
            if end-start == 1: 
                T = False
                if abs(n-array[start]) <= abs(n-array[end]):
                    answer = array[start]
                else:
                    answer = array[end]
            else:
                T = True
        elif array[mid] >= n:
            start,end = start,mid
            if end - start == 1:
                T = False
                if abs(n-array[start]) <= abs(n-array[end]):
                    answer = array[start]
                else:
                    answer = array[end]
            else :
                T = True
            
    return answer