--  a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.
-- dis[lays the score the number of records with the same score

SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;