-- Write your PostgreSQL query statement below
-- select s.user_id, count(c.user_id) as total, count(c.user_id) FILTER (WHERE c.action = 'confirmed') as confirmed
-- from Signups s left join Confirmations c on s.user_id = c.user_id
-- group by s.user_id

-- part 1 solved now I will have to use subquery to calculate main division. 
select user_id, round(coalesce(confirmed::numeric/nullif(total, 0),0),2) as confirmation_rate from (
    select s.user_id, count(c.user_id) as total, count(c.user_id) FILTER (WHERE c.action = 'confirmed') as confirmed
    from Signups s left join Confirmations c on s.user_id = c.user_id
    group by s.user_id
) as sub