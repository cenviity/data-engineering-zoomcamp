with

trips as (

	select
		cast(lpep_pickup_datetime as date) as pickup_date,
		"PULocationID" as pickup_location_id,
        total_amount

	from green_taxi_trips

),

boroughs as (

    select
        "LocationID" as location_id,
        "Borough" as borough

    from zones

),

joined as (

    select
        trips.pickup_date,
        boroughs.borough,

        sum(trips.total_amount) as total_amount

    from trips

    left join boroughs
        on trips.pickup_location_id = boroughs.location_id

    group by
        1,
        2

),

final as (

    select
        pickup_date,
        borough,
        total_amount

    from joined

    where
        pickup_date = '2019-09-18'
        and borough <> 'Unknown'
        and total_amount > 50000

    order by 3 desc

)

select * from final
