SELECT
    a1.name
FROM
    Employee a1
JOIN
    Employee a2
ON
    a1.id = a2.managerId
GROUP BY
    a1.id
HAVING
    COUNT(a1.id) >= 5