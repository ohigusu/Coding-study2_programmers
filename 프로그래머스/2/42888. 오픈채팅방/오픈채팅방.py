def solution(record):
    name_map = {}
    actions = []   
    for rec in record:
        parts = rec.split()
        cmd = parts[0]
        uid = parts[1]
        if cmd == "Enter":
            nick = parts[2]
            name_map[uid] = nick
            actions.append((cmd, uid))
        elif cmd == "Leave":
            actions.append((cmd, uid))
        else:
            nick = parts[2]
            name_map[uid] = nick

    answer = []
    for cmd, uid in actions:
        nick = name_map[uid]
        if cmd == "Enter":
            answer.append(f"{nick}님이 들어왔습니다.")
        else:  # Leave
            answer.append(f"{nick}님이 나갔습니다.")

    return answer
