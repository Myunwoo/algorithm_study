SELECT
    a1.employee_id
    , a1.name
    , COUNT(a2.employee_id) AS reports_count
    , ROUND(AVG(a2.age)) AS average_age
FROM
    Employees a1
JOIN (
    SELECT
        employee_id
        , reports_to
        , age
    FROM
        Employees
    WHERE
        reports_to IS NOT NULL
) a2
ON
    a1.employee_id = a2.reports_to
GROUP BY
    a1.employee_id
ORDER BY
    a1.employee_id