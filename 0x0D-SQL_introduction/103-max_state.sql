<<<<<<< HEAD
<<<<<<< HEAD
-- Displays the max temperature of each state, ordered by state name.
=======
splays the max temperature of each state, ordered by state name.
>>>>>>> e7501c79315504f111118088e7ff4b37e64e8210
=======
splays the max temperature of each state, ordered by state name.
>>>>>>> e7501c79315504f111118088e7ff4b37e64e8210
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
