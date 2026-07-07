SELECT
    DISTINCT a1.num AS ConsecutiveNums
FROM
    Logs a1
JOIN
    Logs a2
ON
    a1.id = a2.id - 1
JOIN
    Logs a3
ON
    a1.id = a3.id - 2
WHERE
    a1.num = a2.num
    AND a2.num = a3.num