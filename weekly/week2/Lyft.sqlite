-- Retrieve all records from the trips table
SELECT * FROM trips;

-- Retrieve all records from the riders table
SELECT * FROM riders;

-- Retrieve all records from the cars table
SELECT * FROM cars;

-- Combine trip and rider information using a LEFT JOIN
SELECT *
FROM trips
LEFT JOIN riders ON trips.rider_id = riders.id;

-- Link trips with the cars used using an INNER JOIN
SELECT *
FROM trips
JOIN cars ON trips.car_id = cars.id;

-- Combine records from riders and riders2 tables
SELECT *
FROM riders
UNION
SELECT *
FROM riders2;

-- Calculate the average cost of trips
SELECT AVG(cost) AS average_trip_cost
FROM trips;

-- Find riders with fewer than 500 trips from both riders and riders2
SELECT *
FROM riders
WHERE total_trips < 500
UNION
SELECT *
FROM riders2
WHERE total_trips < 500;

-- Count the number of active cars
SELECT COUNT(*) AS active_cars_count
FROM cars
WHERE status = 'active';

-- Retrieve the two cars with the highest number of completed trips
SELECT *
FROM cars
ORDER BY trips_completed DESC
LIMIT 2;
