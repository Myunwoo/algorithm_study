SELECT
    MAX(a1.num) AS num
FROM (
    SELECT
        num
    FROM
        MyNumbers
    GROUP BY
        num
    HAVING
        COUNT(num) = 1
) a1
