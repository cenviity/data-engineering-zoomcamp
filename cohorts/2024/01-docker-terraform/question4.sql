with

trips as (

    select
        cast(lpep_pickup_datetime as date) as pickup_date,
        trip_distance

    from green_taxi_trips

),

final as (

    select
        pickup_date,
        max(trip_distance)

    from trips

    group by 1

    order by 2 desc

    limit 1

)

select * from final
