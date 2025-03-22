from collections import deque
def solution(cacheSize, cities):
    # 도시 이름 검색 -> 해당 도시와 관련된 맛집 게시물들을 데이터베이스에서 읽어 보여주는 서비스
    time = 0
    cache = deque()

    for city in cities:
        city = city.lower()  
        if city in cache:  # 캐시 hit!
            cache.remove(city)  # 기존 위치에서 제거
            cache.append(city)  # 맨 뒤에 넣음 (최근 사용)
            time += 1
        else:  # 캐시 miss!
            if cacheSize > 0:
                if len(cache) >= cacheSize:
                    cache.popleft()  # 오래된 것 제거
                cache.append(city)  # 새 도시 추가
            time += 5  # DB에서 새로 꺼내오기

    return time
