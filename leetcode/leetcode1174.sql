SELECT
    ROUND(SUM(
        CASE
            WHEN a1.order_date = a1.customer_pref_delivery_date THEN 1
            ELSE 0
        END) / COUNT(a1.customer_id) * 100, 2) AS immediate_percentage
FROM
    Delivery a1
JOIN (
    SELECT
        b1.customer_id
        , MIN(b1.order_date) AS order_date
    FROM
        Delivery b1
    GROUP BY
        b1.customer_id
) a2
ON
    a1.customer_id = a2.customer_id
    AND a1.order_date = a2.order_date