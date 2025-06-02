N,C=map(int,input().strip().split())
M = int(input().strip())
boxes = [tuple(map(int, input().split())) for _ in range(M)]
boxes.sort(key=lambda x: (x[1], x[0]))

remain = [C] * (N)

answer = 0
for send, receive, box in boxes:
    diff = receive-send
    can_send = min(box, min(remain[send:send+diff]))

    if can_send > 0:
        for i in range(send, send+diff):
            remain[i] -= can_send
        answer += can_send
print(answer)
