-- 코드를 입력하세요
# 대여 중인 자동차들의 정보: CRCC(CAR_ID,CAR_TYPE)
# 자동차 대여 기록 정보: CRCRH (CAR_ID)
# 자동차 종류 별 대여 기간 종류 별 할인 정책 정보: CRCDP (CAR_TYPE)

## 자동차 종류가 '트럭'인 자동차의 대여 기록
## 대여 기록 별로 대여 금액(컬럼명: FEE)
## 대여 기록 ID와 대여 금액 리스트
## 대여 금액을 기준으로 내림차순 정렬,대여 기록 ID를 기준으로 내림차순
SELECT HISTORY_ID,TRUNCATE((1- (IFNULL(DISCOUNT_RATE,0) *0.01)) * DAILY_FEE * TIME,0) AS FEE
FROM    (SELECT CH.*,CR.DAILY_FEE,CR.CAR_TYPE, TIMESTAMPDIFF(day,CH.START_DATE,CH.END_DATE) +1 AS TIME,
            CASE 
                WHEN 90 <= TIMESTAMPDIFF(day,CH.START_DATE,CH.END_DATE) THEN '90'
                WHEN 30 <= TIMESTAMPDIFF(day,CH.START_DATE,CH.END_DATE) THEN '30'
                WHEN 7  <= TIMESTAMPDIFF(day,CH.START_DATE,CH.END_DATE) THEN '7'
                ELSE '0' END AS DUR
            FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS CH
                INNER JOIN CAR_RENTAL_COMPANY_CAR AS CR
                ON CH.CAR_ID = CR.CAR_ID
            WHERE CR.CAR_TYPE ='트럭' ) AS T2
    LEFT OUTER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS CP
    ON REGEXP_REPLACE(CP.DURATION_TYPE,'[^0-9]+','') = T2.DUR AND CP.CAR_TYPE = T2.CAR_TYPE
ORDER BY FEE DESC, HISTORY_ID DESC