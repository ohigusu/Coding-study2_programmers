-- 코드를 입력하세요
SELECT MCDP_CD AS '진료과 코드'
      ,COUNT(APNT_NO) AS '5월예약건수'
FROM APPOINTMENT
WHERE MONTH(APNT_YMD) = '05'
    AND YEAR(APNT_YMD) = '2022'
    AND APNT_CNCL_YN = 'N'
GROUP BY MCDP_CD
ORDER BY COUNT(APNT_NO) ASC, MCDP_CD ASC
