# Write your MySQL query statement below
select s.name
from orders o
join company c on c.com_id = o.com_id and c.name = 'red'
right join salesperson s on s.sales_id = o.sales_id
where o.sales_id is null