<<<<<<< HEAD
<<<<<<< HEAD
-- Lists the number of records with the same score in the table second_table.
=======
sts the number of records with the same score in the table second_table.
>>>>>>> e7501c79315504f111118088e7ff4b37e64e8210
=======
sts the number of records with the same score in the table second_table.
>>>>>>> e7501c79315504f111118088e7ff4b37e64e8210
-- Records are ordered by descending count.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
