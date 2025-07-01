SELECT *
FROM startups;

SELECT COUNT(*) as total_companies
FROM startups;

SELECT SUM(valuation) as total_value
FROM startups;

SELECT MAX(raised) as highest_amount
FROM startups;

SELECT MAX(raised) as highest_seed_funding
FROM startups
WHERE stage = 'Seed';

SELECT MIN(founded) as oldest_company
FROM startups;

SELECT AVG(valuation) as avg_valuation
FROM startups;

SELECT category, AVG(valuation) as avg_val_category
FROM startups
GROUP BY category;

SELECT category, ROUND(AVG(valuation), 2) as avg_val_category_round
FROM startups
GROUP BY 1
ORDER BY 2 DESC;

SELECT category, COUNT(*) as company_per_category
FROM startups
GROUP BY category;

SELECT category, COUNT(*) as top_three
FROM startups
GROUP BY category
HAVING COUNT(*) > 3; 

SELECT location, AVG(employees) as employee_per_location
FROM startups
GROUP BY location;

SELECT location, AVG(employees) as big_company_per_location
FROM startups
GROUP BY location
HAVING AVG(employees) > 500;
