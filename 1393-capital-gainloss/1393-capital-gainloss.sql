# Write your MySQL query statement below
SELECT stock_name, SUM(CASE when operation = 'Sell' then price else -price end) as capital_gain_loss
from Stocks
group by stock_name