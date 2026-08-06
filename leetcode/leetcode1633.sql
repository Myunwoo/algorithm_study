SELECT
    contest_id,
    ROUND(
        COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Users),
        2
    ) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY
    percentage DESC,
    contest_id ASC;

SELECT
    a1.contest_id AS contest_id
    , ROUND(COUNT(a2.user_id) / (SELECT COUNT(*) FROM Users) * 100, 2) AS percentage
FROM
    Register a1
JOIN
    Users a2
ON
    a1.user_id = a2.user_id
GROUP BY
    a1.contest_id
ORDER BY
    percentage DESC
    , a1.contest_id ASC