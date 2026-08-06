SELECT
    id
    , movie
    , description
    , rating
FROM
    Cinema
WHERE 1=1
    AND id % 2 != 0
    AND description != 'boring'
ORDER BY
    rating DESC