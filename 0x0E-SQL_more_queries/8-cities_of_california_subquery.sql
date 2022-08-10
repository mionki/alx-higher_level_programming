-- a script that lists all cities of california in hbtn_0d_usa.ADD

-- Results are ordered by ascending cities.id.
SELECT `id`, `name`
  FROM cities
 WHERE `state_id` IN
       (SELECT `id`
	  FROM states
	 WHERE `name` = "California")
 ORDER BY `id`;