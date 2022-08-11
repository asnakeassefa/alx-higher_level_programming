-- displaying ava tempreture by city
SELECT city,AVA(value) AS avg_temp FROM tempretures GROUP BY value ORDER BY AVA(value)