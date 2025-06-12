-- 코드를 입력하세요
# 2021년에 가입
# 상품을 구매한 회원수와 상품을 구매한 회원의 비율 
#   -> 년, 월 별로
#   -> 소수점 두번째자리에서 반올림
# 년을 기준으로 오름차순 정렬, 월을 기준으로 오름차순 정렬

SELECT
    YEAR(o.SALES_DATE) AS YEAR,
    MONTH(o.SALES_DATE) AS MONTH,
    COUNT(DISTINCT o.USER_ID) AS PURCHASED_USERS,
    ROUND(
      COUNT(DISTINCT o.USER_ID)
      / (SELECT COUNT(*) 
         FROM USER_INFO 
         WHERE YEAR(JOINED) = 2021)
    , 1) AS PURCHASED_RATIO
FROM USER_INFO AS u
INNER JOIN ONLINE_SALE AS o
  ON o.USER_ID = u.USER_ID
WHERE YEAR(u.JOINED) = 2021
GROUP BY
    YEAR(o.SALES_DATE),
    MONTH(o.SALES_DATE)
ORDER BY
    YEAR ASC,
    MONTH ASC;
