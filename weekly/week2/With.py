WITH previous_query AS (
   SELECT customer_id,
      COUNT(subscription_id) AS 'subscriptions'
   FROM orders
   GROUP BY customer_id
)
SELECT customers.customer_name, 
   previous_query.subscriptions
FROM previous_query
JOIN customers
  ON previous_query.customer_id = customers.customer_id;

-- WITH statement allows us to perform a separate query (such as aggregating customer’s subscriptions)
-- previous_results is the alias that we will use to reference any columns from the query inside of the WITH clause
-- We can then go on to do whatever we want with this temporary table (such as join the temporary table with another table)
