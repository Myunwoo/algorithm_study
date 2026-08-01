SELECT
    name
FROM
    Customer
WHERE 1=1
    AND referee_id IS NULL
    OR referee_id != 2