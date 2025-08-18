# Write your MySQL query statement below

select e.name as Employee
from Employee e inner join Employee b
on e.managerId=b.id
where e.salary>b.salary;