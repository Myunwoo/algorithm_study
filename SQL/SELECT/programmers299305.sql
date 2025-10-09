SELECT
    ed.ID,
    (SELECT COUNT(*) FROM ECOLI_DATA AS edd WHERE edd.PARENT_ID = ed.ID) AS CHILD_COUNT
FROM
    ECOLI_DATA AS ed
ORDER BY
    ed.ID




# 최초 작성본은 아래.
SELECT ed.ID, COUNT(SELECT * FROM ECOLI_DATA AS edd WHERE edd.PARENT_ID = ed.ID) AS CHILD_COUNT FROM ECOLI_DATA AS ed ORDER BY ed.ID

# 틀린 이유
# COUNT(SELECT …)가 문법적으로 틀렸기 때문이에요.
# COUNT()는 컬럼/표현식을 인자로 받습니다. SELECT(서브쿼리)를 COUNT() 안에 넣을 수 없고, 서브쿼리는 그 자체가 스칼라 값(한 행 한 컬럼)으로 써야 합니다.