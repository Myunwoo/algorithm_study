select
    name
from
    Customer
where 1=1
    and referee_id is null
    or referee_id != 2