<<<<<<< HEAD
-- Lists all records in the table second_table with a score >= 10.
=======
sts all records in the table second_table with a score >= 10.
>>>>>>> e7501c79315504f111118088e7ff4b37e64e8210
-- Records are ordered by descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
