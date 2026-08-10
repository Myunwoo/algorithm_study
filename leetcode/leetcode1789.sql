SELECT
    employee_id
    , department_id
FROM
    Employee
WHERE
    primary_flag = "Y"
    OR employee_id IN (
        SELECT
            employee_id
        FROM
            Employee
        GROUP BY
            employee_id
        HAVING
            COUNT(department_id) = 1
    )


SELECT
    a1.employee_id
    , a1.department_id
FROM
    Employee a1
LEFT JOIN (
    SELECT
        b1.employee_id
    FROM
        Employee b1
    GROUP BY
        b1.employee_id
    HAVING
        COUNT(department_id) = 1
) a2
ON
    a1.employee_id = a2.employee_id
WHERE 1=1
    AND a2.employee_id IS NOT NULL
    OR a1.primary_flag = 'Y'
