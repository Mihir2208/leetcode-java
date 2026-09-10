-- Write your PostgreSQL query statement below
select unique_id, name from Employees as E left join EmployeeUNI as EN on E.id = EN.id