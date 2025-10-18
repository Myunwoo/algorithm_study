SELECT
    COUNT(*) AS FISH_COUNT,
    MAX(a.LENGTH) AS MAX_LENGTH,
    a.FISH_TYPE AS FISH_TYPE
FROM
    (
        SELECT
            CASE 
                WHEN LENGTH IS NULL THEN 10
                ELSE LENGTH
            END AS LENGTH,
            FISH_TYPE
        FROM
            FISH_INFO
    ) AS a
GROUP BY
    a.FISH_TYPE
HAVING
    AVG(a.LENGTH) >= 33
ORDER BY
    a.FISH_TYPE