create database cab_travel;

use cab_travel;


-- 1. View full table
SELECT * FROM details;

-- 2. Total records
SELECT COUNT(*) AS total_trips
FROM details;

-- 3. Check null values
SELECT *
FROM details
WHERE purpose IS NULL;

-- 4. Distinct categories
SELECT DISTINCT category
FROM details;


-- 5. Distinct purposes
SELECT DISTINCT purpose
FROM details;

-- 6. Top starting locations
SELECT start, COUNT(*) AS trip_count
FROM details
GROUP BY start
ORDER BY trip_count DESC;

-- 7. Top destination locations
SELECT stop, COUNT(*) AS trip_count
FROM details
GROUP BY stop
ORDER BY trip_count DESC;

-- 8. Most frequent routes
SELECT start, stop, COUNT(*) AS route_count
FROM details
GROUP BY start, stop
ORDER BY route_count DESC;

-- 9. Average miles traveled
SELECT AVG(miles) AS avg_miles
FROM details;

-- 10. Maximum trip distance
SELECT MAX(miles) AS max_trip
FROM details;

-- 11. Minimum trip distance
SELECT MIN(miles) AS min_trip
FROM details;

-- 12. Long distance trips
SELECT *
FROM details
WHERE miles > 20;

-- 13. Trips by category
SELECT category, COUNT(*) AS total
FROM details
GROUP BY category;

-- 14. Trips by purpose
SELECT purpose, COUNT(*) AS total
FROM details
GROUP BY purpose
ORDER BY total DESC;

-- 15. Total miles by category
SELECT category, SUM(miles) AS total_miles
FROM details
GROUP BY category;

-- 16. Total miles by purpose
SELECT purpose, SUM(miles) AS total_miles
FROM details
GROUP BY purpose
ORDER BY total_miles DESC;

-- 17. Extract trip hour
SELECT HOUR(start_date) AS trip_hour, COUNT(*) AS total_trips
FROM details
GROUP BY trip_hour
ORDER BY trip_hour;

-- 18. Peak travel hour
SELECT HOUR(start_date) AS trip_hour, COUNT(*) AS total_trips
FROM details
GROUP BY trip_hour
ORDER BY total_trips DESC;

-- 19. Trips by day
SELECT DAYNAME(start_date) AS trip_day, COUNT(*) AS total_trips
FROM details
GROUP BY trip_day
ORDER BY total_trips DESC;

-- 20. Trips by month
SELECT MONTHNAME(start_date) AS trip_month, COUNT(*) AS total_trips
FROM details
GROUP BY trip_month
ORDER BY total_trips DESC;

-- 21. Trip duration in minutes
SELECT start_date, end_date,
TIMESTAMPDIFF(MINUTE, start_date, end_date) AS trip_duration
FROM details;

-- 22. Long duration trips
SELECT *,
TIMESTAMPDIFF(MINUTE, start_date, end_date) AS trip_duration
FROM details
ORDER BY trip_duration DESC;

-- 23. Business trips only
SELECT *
FROM details
WHERE category = 'Business';

-- 24. Personal trips only
SELECT *
FROM details
WHERE category = 'Personal';

-- 25. Average trip duration
SELECT AVG(TIMESTAMPDIFF(MINUTE, start_date, end_date)) AS avg_duration
FROM details;

-- 26. Trips starting and ending same place
SELECT *
FROM details
WHERE start = stop;

-- 27. Trips starting and ending different places
SELECT *
FROM details
WHERE start <> stop;

-- 28. Top 10 longest trips
SELECT *
FROM details
ORDER BY miles DESC
LIMIT 10;

-- 29. Route total miles
SELECT start, stop, SUM(miles) AS total_miles
FROM details
GROUP BY start, stop
ORDER BY total_miles DESC;

-- 30. Most common business purpose
SELECT purpose, COUNT(*) AS total
FROM details
WHERE category = 'Business'
GROUP BY purpose
ORDER BY total DESC;