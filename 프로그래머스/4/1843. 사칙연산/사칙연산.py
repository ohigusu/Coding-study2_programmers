def solution(arr):
    nums = list(map(int, arr[0::2]))
    ops = arr[1::2]
    n = len(nums)
    
    dp_min = [[0]*n for _ in range(n)]
    dp_max = [[0]*n for _ in range(n)]
    
    for i in range(n):
        dp_min[i][i] = dp_max[i][i] = nums[i]
    
    for length in range(2,n+1):
        for i in range(0,n-length+1):
            j = i+length-1
            mn = float('inf')
            mx = float('-inf')
            
            for k in range(i, j):
                op = ops[k]
                a_min, a_max = dp_min[i][k], dp_max[i][k]
                b_min, b_max = dp_min[k+1][j], dp_max[k+1][j]

                if op == '+':
                    cand_min = a_min + b_min
                    cand_max = a_max + b_max
                else:  # op == '-'
                    cand_min = a_min - b_max
                    cand_max = a_max - b_min

                if cand_min < mn: mn = cand_min
                if cand_max > mx: mx = cand_max

            dp_min[i][j] = mn
            dp_max[i][j] = mx

    return dp_max[0][n-1]
