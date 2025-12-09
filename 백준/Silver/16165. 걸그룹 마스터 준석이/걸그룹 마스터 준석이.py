import sys
input = sys.stdin.readline

N, M = map(int, input().split())

name_to_team = {}
team_to_names = {}

# 그룹 정보 입력
for _ in range(N):
    team = input().strip()        # 팀 이름
    rep = int(input())            # 멤버 수
    members = []
    for _ in range(rep):
        name = input().strip()
        name_to_team[name] = team
        members.append(name)
    members.sort()                # 사전순 정렬
    team_to_names[team] = members

# 쿼리 처리
for _ in range(M):
    mm = input().strip()          # 이름 또는 팀
    m = int(input())              # 0 or 1
    if m == 1:
        # 이름이 주어짐 → 팀 이름 출력
        print(name_to_team[mm])
    else:
        # 팀 이름이 주어짐 → 멤버들 이름 사전순 출력
        for member in team_to_names[mm]:
            print(member)
