SELECT
    user_id
    , CONCAT(UPPER(SUBSTRING(name, 1, 1)), LOWER(SUBSTRING(name,2))) AS name
FROM
    Users
ORDER BY
    user_id


SELECT
    user_id
    , CONCAT(UPPER(SUBSTR(name, 1, 1)), LOWER(SUBSTR(name, 2))) AS name
FROM
    Users
ORDER BY
    user_id ASC