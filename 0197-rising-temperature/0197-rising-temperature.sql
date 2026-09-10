# Write your MySQL query statement below
SELECT t.id
FROM weather t
INNER JOIN weather y
ON DATEDIFF(t.recordDate, y.recordDate) = 1
WHERE t.temperature > y.temperature;