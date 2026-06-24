SELECT
    a1.id as id
FROM
    Weather a1
JOIN
    Weather a2
ON
    a1.recordDate = ADDDATE(a2.recordDate, INTERVAL 1 DAY)
where a1.temperature > a2.temperature