SELECT
    DISTINCT author_id AS id
FROM
    Views
WHERE 1=1
    AND author_id = viewer_id
ORDER BY id ASC