-- displaying ava tempreture by city
SELECT * FROM (SELECT city,AVG('value') AS avg_temp FROM temperatures GROUP BY city) AS T ORDER BY avg_temp DESC