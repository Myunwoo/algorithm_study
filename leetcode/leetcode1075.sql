SELECT
    a1.project_id
    , ROUND(AVG(a2.experience_years), 2) as average_years
FROM
    Project a1
JOIN
    Employee a2
ON
    a1.employee_id = a2.employee_id
GROUP BY
    a1.project_id