-- 코드를 작성해주세요
SELECT a.ID
      ,b.FISH_NAME
      ,a.LENGTH AS LENGTH
FROM FISH_INFO AS a
    INNER JOIN FISH_NAME_INFO AS b ON a.FISH_TYPE = b.FISH_TYPE
WHERE (a.FISH_TYPE,a.LENGTH) IN (SELECT fi.FISH_TYPE
                                     ,MAX(fi.LENGTH) AS max_len
                                 FROM FISH_INFO AS fi
                                 GROUP BY fi.FISH_TYPE
                                 HAVING max_len IS NOT NULL)

