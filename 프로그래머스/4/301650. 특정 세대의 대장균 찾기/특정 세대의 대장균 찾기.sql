-- 코드를 작성해주세요.
WITH RECURSIVE CTE AS(
    #앵커 멤버
    SELECT ID, 1 AS GENERATION
    FROM ECOLI_DATA 
    WHERE PARENT_ID IS NULL
    
    UNION ALL
    
    #재귀 멤버
    SELECT CHILD.ID, CTE.GENERATION + 1 AS GENERATION
    FROM ECOLI_DATA AS CHILD
        INNER JOIN CTE ON CHILD.PARENT_ID = CTE.ID
)

SELECT ID
FROM CTE
WHERE GENERATION = 3
ORDER BY ID;

