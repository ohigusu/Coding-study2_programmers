-- 코드를 입력하세요
SELECT CAR_TYPE
      ,COUNT(DISTINCT CAR_ID) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE '%통풍시트%'
    OR OPTIONS LIKE '%열선시트%'
    OR OPTIONS LIKE '%가죽시트' 
    #'통풍시트', '열선시트', '가죽시트' 중 하나 이상의 옵션이 포함된 자동차
GROUP BY CAR_TYPE #자동차 종류 별
ORDER BY CAR_TYPE ASC
