-- displaying Top 3 ava tempreture by city 
SELECT city, avg_temp FROM (SELECT city,AVG(value) AS avg_temp FROM temperatures GROUP BY city) AS T WHERE month IN (7,8) ORDER BY avg_temp DESC;