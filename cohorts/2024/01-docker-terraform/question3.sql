with

trips as (

    select
        cast(lpep_pickup_datetime as date) as pickup_date,
        cast(lpep_dropoff_datetime as date) as dropoff_date

    from green_taxi_trips

),

final as (

    select
        pickup_date,
        dropoff_date,
        count(*)

    from
        trips

    where
        pickup_date = '2019-09-18'
        and dropoff_date = '2019-09-18'

    group by
        1,
        2

)

select * from final
