SELECT
    ROUND(
        SUM(
            CASE
                WHEN a1.order_date = a1.customer_pref_delivery_date THEN 1
                ELSE 0
            END
        ) / COUNT(*) * 100,
        2
    ) AS immediate_percentage
FROM Delivery a1
JOIN (
    SELECT
        customer_id,
        MIN(order_date) AS first_order_date
    FROM Delivery
    GROUP BY customer_id
) a2
ON a1.customer_id = a2.customer_id
AND a1.order_date = a2.first_order_date;