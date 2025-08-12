def solution(routes):
    # 1) 진출 지점 기준으로 정렬
    routes.sort(key=lambda x: x[1])

    cameras = 0
    camera_pos = -30001  # 최소 시작점(-30000)보다 작은 값으로 초기화

    for s, e in routes:
        # 현재 카메라가 이 차량 구간에 포함되지 않으면 새 카메라를 설치
        # 포함 조건: s <= camera_pos <= e
        # 따라서 새 카메라 필요 조건: camera_pos < s
        if camera_pos < s:
            cameras += 1
            camera_pos = e  # 해당 차량의 '진출 지점'에 설치

    return cameras