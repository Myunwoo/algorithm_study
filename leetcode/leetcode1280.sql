SELECT
    a1.student_id AS student_id
    , a1.student_name AS student_name
    , a2.subject_name AS subject_name
    , COUNT(a3.student_id) AS attended_exams
FROM
    Students a1
CROSS JOIN
    Subjects a2
LEFT JOIN
    Examinations a3
ON
    a1.student_id = a3.student_id
    AND a2.subject_name = a3.subject_name
GROUP BY
    a1.student_id
    , a2.subject_name
ORDER BY
    student_id
    , subject_name