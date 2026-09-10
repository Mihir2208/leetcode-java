-- Write your PostgreSQL query statement below
select l.machine_id, round(cast(avg(r.timestamp-l.timestamp)AS numeric),3) as processing_time from Activity l 
join Activity r on l.process_id = r.process_id and l.machine_id = r.machine_id
where l.activity_type = 'start' and r.activity_type='end'
group by l.machine_id