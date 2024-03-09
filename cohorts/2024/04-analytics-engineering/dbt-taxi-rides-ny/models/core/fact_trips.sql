{{
    config(
        materialized='table'
    )
}}

with

green_tripdata as (

    select
        *,
        'Green' as service_type

    from {{ ref('stg_green_taxi_trips') }}

),

yellow_tripdata as (

    select
        *,
        'Yellow' as service_type

    from {{ ref('stg_yellow_taxi_trips') }}

),

trips_unioned as (

    select * from green_tripdata

    union all

    select * from yellow_tripdata

),

dim_zones as (

    select * from {{ ref('dim_zones') }}

    where borough != 'Unknown'

)

select
    trips_unioned.tripid,
    trips_unioned.vendorid,
    trips_unioned.service_type,
    trips_unioned.ratecodeid,

    trips_unioned.pickup_locationid,
    pickup_zones.borough as pickup_borough,
    pickup_zones.zone as pickup_zone,

    trips_unioned.dropoff_locationid,
    dropoff_zones.borough as dropoff_borough,
    dropoff_zones.zone as dropoff_zone,

    trips_unioned.pickup_datetime,
    trips_unioned.dropoff_datetime,
    trips_unioned.store_and_fwd_flag,
    trips_unioned.passenger_count,
    trips_unioned.trip_distance,
    trips_unioned.trip_type,
    trips_unioned.fare_amount,
    trips_unioned.extra,
    trips_unioned.mta_tax,
    trips_unioned.tip_amount,
    trips_unioned.tolls_amount,
    trips_unioned.ehail_fee,
    trips_unioned.improvement_surcharge,
    trips_unioned.total_amount,
    trips_unioned.payment_type,
    trips_unioned.payment_type_description

from trips_unioned

inner join dim_zones as pickup_zones
    on trips_unioned.pickup_locationid = pickup_zones.locationid

inner join dim_zones as dropoff_zones
    on trips_unioned.pickup_locationid = dropoff_zones.locationid
