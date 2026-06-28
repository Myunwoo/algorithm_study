SELECT
    a1.query_name
    , ROUND(AVG(a1.rating / a1.position), 2) AS quality
    , IFNULL(ROUND(SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) / COUNT(*) * 100, 2), 0) AS poor_query_percentage
FROM
    Queries a1
GROUP BY
    query_name
