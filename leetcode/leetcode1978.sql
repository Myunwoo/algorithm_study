SELECT
    a1.employee_id
FROM
    Employees a1
WHERE
    salary < 30000
    AND NOT EXISTS (
        SELECT
            a2.employee_id
        FROM
            Employees a2
        WHERE
            a1.manager_id = a2.employee_id
    )
    AND manager_id IS NOT NULL
ORDER BY
    a1.employee_id