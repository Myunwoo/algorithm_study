SELECT
    a2.unique_id
    , a1.name
FROM
    Employees a1
LEFT JOIN
    EmployeeUNI a2
ON
    a1.id = a2.id
