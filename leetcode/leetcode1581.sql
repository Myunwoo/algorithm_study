SELECT
    a1.customer_id
    , COUNT(a1.customer_id) as count_no_trans
FROM
    Visits a1
LEFT JOIN
    Transactions a2
ON
    a1.visit_id = a2.visit_id
WHERE
    a2.transaction_id IS NULL
GROUP BY
    a1.customer_id