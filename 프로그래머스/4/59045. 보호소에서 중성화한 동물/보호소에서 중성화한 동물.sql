WITH intact_ins AS (
    SELECT
        ANIMAL_ID,
        ANIMAL_TYPE,
        NAME
    FROM
        ANIMAL_INS
    WHERE
        SEX_UPON_INTAKE LIKE 'Intact %'
)
SELECT
    i.ANIMAL_ID,
    i.ANIMAL_TYPE,
    i.NAME
FROM
    intact_ins AS i
    INNER JOIN ANIMAL_OUTS AS o
        ON i.ANIMAL_ID = o.ANIMAL_ID
WHERE
    o.SEX_UPON_OUTCOME LIKE 'Neutered %'  -- 퇴소 당시 중성화(수컷)
    OR o.SEX_UPON_OUTCOME LIKE 'Spayed %'
ORDER BY
    i.ANIMAL_ID;