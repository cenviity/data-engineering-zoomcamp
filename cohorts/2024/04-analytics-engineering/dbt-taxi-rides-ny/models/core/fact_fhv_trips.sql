{{
    config(
        materialized='table'
    )
}}

with

fhv_tripdata as (

    select
        *,
        "FHV" as service_type

    from {{ ref("stg_fhv_taxi_trips") }}

),

dim_zones as (

    select * from {{ ref("dim_zones") }}

    where borough != "Unknown"

)

select
    fhv_tripdata.tripid,
    fhv_tripdata.dispatching_base_number,
    fhv_tripdata.service_type,

    fhv_tripdata.pickup_locationid,
    pickup_zones.borough as pickup_borough,
    pickup_zones.zone as pickup_zone,

    fhv_tripdata.dropoff_locationid,
    dropoff_zones.borough as dropoff_borough,
    dropoff_zones.zone as dropoff_zone,

    fhv_tripdata.pickup_datetime,
    fhv_tripdata.dropoff_datetime,
    fhv_tripdata.shared_ride_flag,
    fhv_tripdata.affiliated_base_number

from fhv_tripdata

inner join dim_zones as pickup_zones
    on fhv_tripdata.pickup_locationid = pickup_zones.locationid

inner join dim_zones as dropoff_zones
    on fhv_tripdata.dropoff_locationid = dropoff_zones.locationid
