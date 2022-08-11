-- displaying Top 3 ava tempreture by city 
SELECT * FROM (SELECT TOP 3 city,AVG(value) AS avg_temp FROM temperatures GROUP BY city HAVING month IN(7,8)) AS T ORDER BY avg_temp;