SELECT
    a1.product_id
    , a2.min_year AS first_year
    , a1.quantity 
    , a1.price
FROM
    Sales a1
JOIN (
    SELECT
        b1.product_id
        , MIN(b1.year) AS min_year
    FROM
        Sales b1
    GROUP BY
        b1.product_id
) a2
ON
    a1.product_id = a2.product_id
    AND a1.year = a2.min_year
