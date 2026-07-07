SELECT
    c.category AS category
    , IFNULL(b.accounts_count, 0) AS accounts_count
FROM (
    SELECT 'Low Salary' AS category
    UNION ALL
    SELECT 'Average Salary'
    UNION ALL
    SELECT 'High Salary'
) c
LEFT JOIN (
    SELECT
        a.category
        , COUNT(a.account_id) AS accounts_count
    FROM (
        SELECT
            account_id
            , income
            , (CASE
                WHEN income < 20000 THEN 'Low Salary'
                WHEN income >= 20000 AND income <= 50000 THEN 'Average Salary'
                WHEN income > 50000 THEN 'High Salary'
            END) AS category
        FROM
            Accounts
    ) a
    GROUP BY
        category
) b
ON
    c.category = b.category