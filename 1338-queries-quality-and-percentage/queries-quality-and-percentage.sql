-- Write your PostgreSQL query statement below
select query_name, round(coalesce(sum(rating::numeric/position)/count(query_name), 0),2) as quality, 
round(coalesce((count(case when rating < 3 then 1 end)::numeric/count(query_name))*100, 0), 2) as poor_query_percentage
from Queries
group by query_name 