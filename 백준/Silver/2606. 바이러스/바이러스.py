from collections import defaultdict
computer =  int(input())
active = int(input())
graph = defaultdict(list)
for _ in range(active):
	start,end=map(int,input().split())
	graph[start].append(end)
	graph[end].append(start)

def dfs(graph,start):
	stack=[start]
	answer=0
	visited = [False]*(computer+1)
	
	while stack:
		node = stack.pop()
		if not visited[node]:
			visited[node]=True	
			answer += 1
			for neighbor in reversed(graph[node]):
				if not visited[neighbor]:
					stack.append(neighbor)
	return answer

answer = dfs(graph,1)
print(answer-1)