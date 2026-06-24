SELECT
    a2.product_name
    , a1.year
    , a1.price
FROM
    Sales a1
JOIN
    Product a2
ON
    a1.product_id = a2.product_id
