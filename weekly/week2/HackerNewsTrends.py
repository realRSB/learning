SELECT title, score
FROM hacker_news
ORDER BY score DESC
LIMIT 5;

SELECT SUM(score) as total_score
FROM hacker_news;

SELECT user, SUM(score) 
FROM hacker_news
GROUP BY user
HAVING SUM(score) > 200
ORDER BY 2 DESC;

SELECT (517+309+394+282)/6;

SELECT user, COUNT(*)
FROM hacker_news
WHERE URL = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
GROUP BY 1
ORDER BY 2 DESC;

SELECT CASE
  WHEN url LIKE '%github.com%' THEN 'GitHub'
  WHEN url LIKE '%medium.com%' THEN 'Medium'
  WHEN url LIKE '%nytimes.com%' THEN 'New York Times'
  ELSE 'Other'
END AS 'Source',
COUNT(*)
FROM hacker_news
GROUP BY 1;

SELECT timestamp
FROM hacker_news
LIMIT 10;

SELECT timestamp,
   strftime('%H', timestamp)
FROM hacker_news
GROUP BY 1
LIMIT 20;

SELECT strftime('%H', timestamp) AS 'Hour', 
   ROUND(AVG(score), 1) AS 'Average Score', 
   COUNT(*) AS 'Number of Stories'
FROM hacker_news
WHERE timestamp IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC;




