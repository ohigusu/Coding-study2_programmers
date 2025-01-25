-- 코드를 입력하세요
WITH RECURSIVE time AS (
    SELECT 0 AS num
    
    UNION ALL
    
    SELECT num + 1
    FROM time
    WHERE num < 23
), ANIMAL_CNT AS (
    SELECT HOUR(DATETIME) AS HOUR
         , COUNT(ANIMAL_ID) AS CNTS
    FROM ANIMAL_OUTS
    GROUP BY HOUR
    ORDER BY HOUR
)

SELECT time.num
     , IFNULL(a.CNTS, 0)
FROM time
    LEFT JOIN ANIMAL_CNT AS a ON time.num = a.HOUR