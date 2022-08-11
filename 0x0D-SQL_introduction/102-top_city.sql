-- displaying Top 3 ava tempreture by city 
SELECT city, avg_temp FROM (SELECT city,AVG(value) AS avg_temp FROM temperatures WHERE month IN (7,8) GROUP BY city) AS T ORDER BY avg_temp DESC LIMIT 3;
