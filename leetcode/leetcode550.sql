SELECT
    ROUND(SUM(CASE WHEN a2.player_id IS NULL THEN 0 ELSE 1 END) / COUNT(DISTINCT a1.player_id), 2) AS fraction
FROM
    Activity a1
LEFT JOIN (
    SELECT
        player_id
        , ADDDATE(MIN(event_date), INTERVAL 1 DAY) AS next_day
    FROM
        Activity
    GROUP BY
        player_id
) a2
ON
    a1.event_date = a2.next_day
    AND a1.player_id = a2.player_id