SELECT
    fh.FLAVOR
FROM
    FIRST_HALF AS fh
INNER JOIN
    (
        SELECT
            FLAVOR,
            SUM(TOTAL_ORDER) AS TOTAL_ORDER
        FROM
            JULY
        GROUP BY
            FLAVOR
    ) AS j
ON
    fh.FLAVOR = j.FLAVOR
ORDER BY
    fh.TOTAL_ORDER + j.TOTAL_ORDER DESC
LIMIT 3
