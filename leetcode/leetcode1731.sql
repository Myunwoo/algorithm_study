SELECT
    a1.employee_id AS employee_id
    , a1.name AS name
    , COUNT(a2.reports_to) AS reports_count
    , ROUND(AVG(a2.age)) AS average_age
FROM
    Employees a1
JOIN
    Employees a2
ON
    a1.employee_id = a2.reports_to
GROUP BY
    a1.employee_id
ORDER BY
    a1.employee_id