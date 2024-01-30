with

trips as (

	select
		cast(lpep_pickup_datetime as date) as pickup_date,
        "PULocationID" as pickup_location_id,
		"DOLocationID" as dropoff_location_id,
        tip_amount

	from green_taxi_trips

),

zones as (

    select
        "LocationID" as location_id,
        "Zone" as zone

    from zones

),

joined as (

    select
        trips.pickup_date,
        pickup_zones.zone as pickup_zone,
        dropoff_zones.zone as dropoff_zone,
        trips.tip_amount

    from trips

    left join zones as pickup_zones
        on trips.pickup_location_id = pickup_zones.location_id

    left join zones as dropoff_zones
        on trips.dropoff_location_id = dropoff_zones.location_id

    where
        trips.pickup_date >= '2019-09-01'
        and trips.pickup_date < '2019-10-01'
        and pickup_zones.zone = 'Astoria'

),

final as (

    select
        dropoff_zone,
        tip_amount

    from joined

    order by 2 desc

    limit 1

)

select * from final
