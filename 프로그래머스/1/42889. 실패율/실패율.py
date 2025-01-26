def solution(N, stages):
    num_player = [0] * N  # [0,0,0,0]
    nonpass_player = [0] * N  # [0,0,0,0]

    for stage in stages:
        if stage <= N:  
            nonpass_player[stage-1] += 1
        for j in range(0, min(stage, N)):  
            num_player[j] += 1
    result = []
    for idx in range(0, N):
        if num_player[idx] == 0:
            failure_rate = 0  
        else:
            failure_rate = nonpass_player[idx] / num_player[idx]
        result.append((failure_rate, idx+1))

    result.sort(key=lambda x: (-x[0], x[1]))

    return [stage for _, stage in result]