with

source as (

    select * from {{ source('staging', 'green_taxi_trips') }}

),

renamed as (

    select
        vendor_id,
        lpep_pickup_datetime,
        lpep_dropoff_datetime,
        store_and_fwd_flag,
        ratecode_id,
        pu_location_id,
        do_location_id,
        passenger_count,
        trip_distance,
        fare_amount,
        extra,
        mta_tax,
        tip_amount,
        tolls_amount,
        ehail_fee,
        improvement_surcharge,
        total_amount,
        {{ get_payment_type_description("payment_type") }} as payment_type_description,
        trip_type,
        congestion_surcharge

    from source

)

select * from renamed
