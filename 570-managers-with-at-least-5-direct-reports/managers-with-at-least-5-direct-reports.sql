-- Write your PostgreSQL query statement below
select m.name from Employee r 
join Employee m on r.managerId = m.id
group by m.name, m.id
having count(m.id)>=5

