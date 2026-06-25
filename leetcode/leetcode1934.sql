SELECT
    a1.user_id
    , (
        CASE
            WHEN a2.user_id IS NULL THEN 0
            ELSE ROUND(SUM(
                CASE
                    WHEN a2.action = 'confirmed' THEN 1
                    ELSE 0
                END
            ) / COUNT(a2.action), 2)
        END
    ) as confirmation_rate 
FROM
    Signups a1
LEFT JOIN
    Confirmations a2
ON
    a1.user_id = a2.user_id
GROUP BY
    a1.user_id