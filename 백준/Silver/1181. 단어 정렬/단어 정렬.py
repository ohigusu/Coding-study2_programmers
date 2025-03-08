N = int(input())
li= []
for _ in range(N):
	word = input()
	li.append(word)
    
set_li = list(set(li))
set_li.sort()
set_li.sort(key=lambda x: len(x))

for i in set_li:
	print(i)