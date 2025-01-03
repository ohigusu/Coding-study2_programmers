-- 코드를 입력하세요
SELECT ugu.USER_ID
      ,ugu.NICKNAME
      ,SUM(ugb.PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD AS ugb
    INNER JOIN USED_GOODS_USER AS ugu ON ugb.WRITER_ID = ugu.USER_ID
WHERE ugb.STATUS='DONE'
GROUP BY ugb.WRITER_ID 
    HAVING SUM(ugb.PRICE) >= 700000 
ORDER BY TOTAL_SALES ASC