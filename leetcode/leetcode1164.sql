SELECT
    DISTINCT d.product_id
    , IFNULL(c.new_price, 10) AS price 
FROM (
    SELECT DISTINCT product_id
    FROM Products
) d
LEFT JOIN (
    SELECT
        a.product_id
        , a.new_price
        , a.change_date
    FROM
        Products a
    JOIN (
        SELECT
            product_id
            , MAX(change_date) AS change_date
        FROM
            Products
        WHERE
            change_date <= '2019-08-16'
        GROUP BY
            product_id
    ) b
    ON
        a.product_id = b.product_id
        AND a.change_date = b.change_date
) c
ON
    d.product_id = c.product_id