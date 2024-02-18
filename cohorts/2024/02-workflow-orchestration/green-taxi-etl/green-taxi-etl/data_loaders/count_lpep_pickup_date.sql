select count(distinct lpep_pickup_date)

from {{ df_1 }}

order by 1
