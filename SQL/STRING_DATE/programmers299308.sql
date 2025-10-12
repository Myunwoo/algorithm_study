select
    case
        when month(DIFFERENTIATION_DATE) between 1 and 3 then '1Q'
        when month(DIFFERENTIATION_DATE) between 4 and 6 then '2Q'
        when month(DIFFERENTIATION_DATE) between 7 and 9 then '3Q'
        else '4Q'
end as 'QUARTER',
    count(id) AS 'ECOLI_COUNT'
from ECOLI_DATA
group by QUARTER
order by QUARTER


-- 논리적 순서상 SELECT가 나중이지만, MySQL은 GROUP BY/ORDER BY에서 SELECT 별칭을 식으로 치환해 주기 때문에 동작합니다.
-- 더 mysql슽럽게 푸는 방법은 아래와 같음
SELECT
  CONCAT(QUARTER(DIFFERENTIATION_DATE), 'Q') AS QUARTER,
  COUNT(*) AS ECOLI_COUNT
FROM ECOLI_DATA
GROUP BY QUARTER
ORDER BY QUARTER;
