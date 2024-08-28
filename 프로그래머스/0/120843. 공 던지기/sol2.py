#numbers: 친구들의 번호
#k: 공이 몇 번째로 던져지는지
#2 * (k - 1): 첫 번째 던짐부터 시작하여 k번째 던짐까지 오른쪽으로 한 명을 건너뛰면서 공을 던질 때의 위치 계산
#% len(numbers): 리스트의 길이를 넘어가는 인덱스를 처리하여 리스트가 원형으로 연결된 것처럼 동작
def solution(numbers, k):
  return numbers[2*(k-1)%len(numbers)]
