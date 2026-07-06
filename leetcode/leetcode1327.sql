SELECT
    (SELECT
        a2.product_name
    FROM
        Products a2
    WHERE
        a1.product_id = a2.product_id) AS product_name
    , SUM(a1.unit) AS unit
FROM
    Orders a1
WHERE
    a1.order_date BETWEEN '20200201000000' AND '20200229235959'
GROUP BY
    a1.product_id
HAVING
    SUM(a1.unit) >= 100