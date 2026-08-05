

SELECT
    a1.name
FROM
    Employee a1
LEFT JOIN
    Employee a2
ON
    a1.id = a2.managerId
GROUP BY
    a1.id
HAVING
    COUNT(a2.managerId) >= 5