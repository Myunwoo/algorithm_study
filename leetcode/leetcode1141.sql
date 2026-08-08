SELECT
    activity_date AS day
    , COUNT(DISTINCT user_id) AS active_users
FROM
    Activity
WHERE
    activity_date <= "2019-07-27"
    AND activity_date >= "2019-06-28"
GROUP BY
    activity_date


SELECT
    activity_date AS day
    , COUNT(DISTINCT user_id) AS active_users
FROM
    Activity
WHERE
    activity_date BETWEEN '2019-06-28' AND '2019-07-27'
GROUP BY
    activity_date

-- 이 문제에서 부등호와 DATETIME은 동일하게 동작한다. 이유는 칼럼 타임이 DATETIME이기 따문(일 까지만을 포함)
-- 하지만 TIMESTAMP라면, BETWEEN을 사용했을 때 00:00:00을 기준으로 동작하므로 부등호를 사용하는 것이 더 직관적인 방법이다.