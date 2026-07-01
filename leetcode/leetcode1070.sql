-- 상품별 첫 판매 연도의 판매 정

SELECT
    a1.product_id
    , a2.min_year AS first_year
    , a1.quantity
    , a1.price
FROM
    Sales a1
JOIN (
    SELECT
        product_id
        , MIN(year) AS min_year
    FROM
        Sales
    GROUP BY
        product_id
) a2
ON
    a1.year = a2.min_year
    AND a1.product_id = a2.product_id