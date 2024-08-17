-- 코드를 입력하세요
/*SELECT NAME 	
FROM ANIMAL_INS
ORDER BY DATETIME LIMIT 1;
*/

SELECT A.NAME 	
FROM ANIMAL_INS AS A
WHERE A.DATETIME = (SELECT MIN(DATETIME) FROM ANIMAL_INS) ;

/*select name from animal_ins a where a.datetime=
(SELECT min(datetime) from animal_ins)*/