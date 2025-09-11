from collections import defaultdict
def solution(genres, plays):
    # 1) 장르별 총 재생 수 집계
    genre_total = defaultdict(int)
    # 2) 장르별 곡 목록 저장: (재생 수, 고유번호)
    songs_by_genre = defaultdict(list)
    
    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_total[g] += p
        songs_by_genre[g].append((p, i))
    
    # 3) 장르를 총 재생 수 내림차순으로 정렬
    genre_order = sorted(genre_total.items(), key=lambda x: -x[1])
    
    answer = []
    for g, _ in genre_order:
        # 4) 장르 내 곡을 (재생 수 내림차순, 고유번호 오름차순)으로 정렬
        songs = sorted(songs_by_genre[g], key=lambda x: (-x[0], x[1]))
        # 5) 최대 2곡 선택
        cnt = 0
        for p, i in songs:
            if cnt < 2:
                answer.append(i)
                cnt += 1
            else:
                break
    return answer
