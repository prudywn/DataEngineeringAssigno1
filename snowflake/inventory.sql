--1. What are the top 5 best-selling products by quantity sold?
use schema retail_data;

select * from fact_sales;

--1. What are the top 5 best-selling products by quantity sold?
select product_name, sum(quantity_sold) as total_sold
from dim_products
join fact_sales on dim_products.product_id = fact_sales.product_id
group by product_name
order by total_sold desc;

--2. Which store generated the highest total revenue in the last 10 days?
select store_name, sum(price * quantity_sold) as total_revenue
from dim_stores
join fact_sales on dim_stores.store_id = fact_sales.store_id
group by store_name
limit 1;

--3. What is the net inventory movement (IN - OUT) for each product?
select product_name,
sum(
case when movement_type = 'IN' then quantity_change  else 0
end) 
-
sum(
case when movement_type = 'OUT' then quantity_change else 0 end
)
AS net_movement
from dim_products
join fact_inventory on dim_products.product_id = fact_inventory.product_id
group by product_name
order by net_movement desc;

--4. On which day of the week do customer interactions occur most frequently?
select dim_time.day_of_the_week, 
count(*) as total_days
from fact_customer_interaction 
join dim_time on dim_time.date_id = fact_customer_interaction.date_id
group by day_of_the_week
order by total_days desc
limit 1;

--5. What is the average customer feedback score per store?
select store_name, avg(feedback_score) as avg_score  
from dim_stores
join fact_customer_interaction on dim_stores.store_id = fact_customer_interaction.store_id
group by store_name
order by avg_score desc;

--6. What is the trend of daily sales revenue over the past 10 days?
select 
  date_id,
  SUM(price * quantity_sold) as daily_revenue
from 
  fact_sales
where 
  date_id >= (select MAX(date_id) - 9 from fact_sales)
group by 
  date_id
order by 
  daily_revenue desc;
