-- displaying Top 3 ava tempreture by city 
SELECT TOP 3 * FROM (SELECT city,AVG(value) AS avg_temp FROM temperatures GROUP BY city) AS T ORDER BY avg_temp DESC