-- 코드를 작성해주세요
WITH cte AS (
SELECT MAX(IF(s.NAME = 'Python',1,0)) AS py
      ,MAX(IF(s.CATEGORY='Front End',1,0)) AS fr
      ,MAX(IF(s.NAME = 'C#',1,0)) AS cs
      ,d.ID
      ,d.EMAIL
FROM DEVELOPERS AS d
    LEFT JOIN SKILLCODES AS s ON (d.SKILL_CODE & s.CODE) =  s.CODE
GROUP BY d.ID,d.EMAIL
)
SELECT *
FROM
(SELECT 
    CASE 
        WHEN py > 0 AND fr > 0 THEN 'A'
        WHEN cs > 0 THEN 'B'
        WHEN fr > 0 THEN 'C'
    END AS GRADE
    ,ID
    ,EMAIL
FROM cte
) AS a
WHERE a.GRADE IS NOT NULL
ORDER BY a.GRADE ASC, a.ID ASC