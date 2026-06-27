SELECT
    a1.product_id
    , IFNULL(ROUND(SUM(a1.price*a2.units) / SUM(a2.units) , 2), 0) as average_price
FROM
    Prices a1
LEFT JOIN
    UnitsSold a2
ON
    a1.product_id = a2.product_id
    AND a1.start_date <= a2.purchase_date
    AND a1.end_date >= a2.purchase_date
GROUP BY
    product_id