SELECT
    id
    , movie
    , description
    , rating
FROM
    Cinema
WHERE 1=1
    AND description != "boring"
    AND id % 2 = 1
ORDER BY
    rating DESC