-- 코드를 입력하세요
SELECT MONTH(START_DATE) AS MONTH
     , CAR_ID
     , COUNT(CAR_ID) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
WHERE month(start_date) BETWEEN 8 AND 10  
    AND car_id in 
(SELECT CAR_ID
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE month(start_date) between 8 and 10  
group by car_id
having count(*) >4
)
group by car_id,month
order by month asc ,car_id desc



