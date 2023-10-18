<<<<<<< HEAD
-- Lists all records of the table second_table having a name value.
=======
sts all records of the table second_table having a name value.
>>>>>>> e7501c79315504f111118088e7ff4b37e64e8210
-- Records are ordered by descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
