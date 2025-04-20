def count_yeonsan(n):
    store = [0] * (n + 1)
    store[1:4] = 0, 1, 1  
    for i in range(4, n + 1):
        cnt = [store[i - 1]] 
        if i % 2 == 0:
            cnt.append(store[i // 2])
        if i % 3 == 0:
            cnt.append(store[i // 3])

        store[i] = 1 + min(cnt)

    return store[n]
N = int(input())
print(count_yeonsan(N))