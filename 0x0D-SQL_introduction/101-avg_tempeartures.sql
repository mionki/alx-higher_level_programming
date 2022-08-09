-- import in hbtn_0c_0 from table dump
-- write a script that displays the average


SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;


