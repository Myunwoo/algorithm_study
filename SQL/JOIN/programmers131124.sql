SELECT
    mp.MEMBER_NAME,
    rr.REVIEW_TEXT,
    DATE_FORMAT(rr.REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM
    REST_REVIEW AS rr
INNER JOIN
    MEMBER_PROFILE AS mp
ON
    rr.MEMBER_ID = mp.MEMBER_ID
WHERE
    rr.MEMBER_ID IN (
        SELECT
            MEMBER_ID
        FROM
            REST_REVIEW
        GROUP BY
            MEMBER_ID
        HAVING
            COUNT(*) = (
                SELECT
                    MAX(C.c)
                FROM (SELECT COUNT(*) AS c FROM REST_REVIEW GROUP BY MEMBER_ID) AS C
            )
    )
ORDER BY
    REVIEW_DATE,
    REVIEW_TEXT