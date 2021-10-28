
with T1 as 
(
SELECT *,
        DATEDIFF(DAY, order_date,shipped_date) Diff_shipped_date

FROM sale.orders
)

SELECT *

from T1
WHERE  diff_shipped_date > 2 

SELECT order_date,
        shipped_date,
        case when Diff_shipped_date is null then 'Not shipped'
            when  Diff_shipped_date = 0 then 'Fast'
            when Diff_shipped_date <= 2 then 'normal'
            when diff_shipped_date > 2 then 'slow'
        end as order_label
from T1



select * ,
        case when datename(WEEKDAY,order_date) = 'Monday' then count(order_date)
        end as Monday

from sale.orders
WHERE DATEDIFF(DAY, order_date,shipped_date) > 2




select order_date,
datename(WEEKDAY,order_date)

from sale.orders
WHERE DATEDIFF(DAY, order_date,shipped_date) > 2



select
        count (case when datename(WEEKDAY,order_date) = 'Monday' then 1
        end) as MONDAY,
        SUM (case when datename(WEEKDAY,order_date) = 'Tuesday' then 1
        end) as TUESDAY,
        SUM (case when datename(WEEKDAY,order_date) = 'Wednesday' then 1
        end) as WEDNESDAY,
        SUM (case when datename(WEEKDAY,order_date) = 'Thursday' then 1
        end) as Thursday,
        SUM (case when datename(WEEKDAY,order_date) = 'Friday' then 1
        end) as Friday,
        SUM (case when datename(WEEKDAY,order_date) = 'Saturday' then 1
        end) as Saturday,
        SUM (case when datename(WEEKDAY,order_date) = 'Sunday' then 1
        end) as Sunday
from sale.orders
WHERE DATEDIFF(DAY, order_date,shipped_date) > 2


Select len('gul neda')



Select len(12468762)

select CHARINDEX('a', 'asfglza',2)

SELECT PATINDEX('%R', 'CHARACTER')

SELECT SUBSTRING('CHARACTER',-1,3)

SELECT SUBSTRING('CHARACTER',1,3)

SELECT TRIM(' ' FROM ' CH ARACTER ')