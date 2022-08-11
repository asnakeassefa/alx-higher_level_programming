-- displaying ava tempreture by city
SELECT city,AVG(value) AS avg_temp FROM temperatures GROUP BY value ORDER BY AVG(value) DESC