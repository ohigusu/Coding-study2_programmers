-- 코드를 입력하세요
SELECT a.AUTHOR_ID
      ,a.AUTHOR_NAME
      ,b.CATEGORY
      ,SUM(bs.SALES*b.PRICE) AS TOTAL_SALES
FROM BOOK AS b
    INNER JOIN BOOK_SALES AS bs ON b.BOOK_ID = bs.BOOK_ID
    INNER JOIN AUTHOR AS a ON b.AUTHOR_ID = a.AUTHOR_ID
WHERE DATE_FORMAT(bs.SALES_DATE,'%Y-%m') = '2022-01' 
GROUP BY a.AUTHOR_NAME, b.CATEGORY
ORDER BY a.AUTHOR_ID ASC,b.CATEGORY DESC