def solution(msg):
    answer = []
    appendix={}
    n = len(msg)
    for i in range(1,27):  
        appendix[chr(i+64)]=i
    last = 26
    
    idx = 0
    while idx < n:
        result_idx = idx
        for j in range(idx,n):
            if msg[idx:j+1] not in appendix:
                break
            result_idx = j

        answer.append(appendix[msg[idx:result_idx+1]])
        
        if result_idx + 1 < n:
            new_entry = msg[idx:result_idx+2]
            if new_entry not in appendix:
                last += 1
                appendix[new_entry] = last
        
        idx = result_idx + 1
    return answer