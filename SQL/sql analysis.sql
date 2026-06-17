SELECT * FROM coffee_sales.coffee_sales;

-- sales column added
select *, round((coffee_sales.transaction_qty * coffee_sales.unit_price), 2) as sale_price
from coffee_sales.coffee_sales;

-- total revenue
select round(sum(sale_price), 2) as total_revenue
from (
	select *, round((coffee_sales.transaction_qty * coffee_sales.unit_price), 2) as sale_price
	from coffee_sales.coffee_sales
    ) as t;
    
-- revenue of stores
select store_location,
       round(sum(transaction_qty * unit_price), 2) as total_revenue
from coffee_sales.coffee_sales
group by store_location
order by total_revenue desc;

-- revenue by product_category
select product_category,
       round(sum(transaction_qty * unit_price), 2) as total_revenue
from coffee_sales.coffee_sales
group by product_category
order by total_revenue desc;

-- sales wrt time
select
    case
        when hour(transaction_time) < 12 then 'Morning'
        when hour(transaction_time) < 17 then 'Afternoon'
        else 'Evening'
    end as time_period,

    count(*) as transactions,

    round(sum(transaction_qty * unit_price), 2) as total_sales

from coffee_sales.coffee_sales
group by time_period
order by total_sales desc;

-- sales wrt month
select
    date_format(transaction_date, '%Y-%m') as month,
    count(*) as total_transactions,
    round(sum(transaction_qty * unit_price), 2) as total_sales
from coffee_sales.coffee_sales
group by month
order by month;

-- sales wrt weekdays
select
    weekday(transaction_date) as weekday_num,
    dayname(transaction_date) as weekday,
    round(sum(transaction_qty * unit_price), 2) as revenue
from coffee_sales.coffee_sales
group by weekday_num, weekday
order by weekday_num;


    
    
    


