<<<<<<< HEAD
-- Displays the 3 cities with the highest average
=======
splays the 3 cities with the highest average
>>>>>>> e7501c79315504f111118088e7ff4b37e64e8210
-- temperatures between July and August.
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;
