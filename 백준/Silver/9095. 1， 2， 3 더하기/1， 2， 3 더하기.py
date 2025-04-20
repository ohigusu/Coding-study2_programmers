T = int(input())

store= [0]*11
store[0] =0
store[1]=1
store[2]=2
store[3]=4
for i in range(4,11):
    store[i] = store[i-1]+store[i-2]+store[i-3]
for _ in range(T):
    n = int(input())
    print(store[n])