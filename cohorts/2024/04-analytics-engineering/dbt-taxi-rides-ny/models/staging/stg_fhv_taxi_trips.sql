with source as (
      select * from {{ source('staging', 'fhv_taxi_trips') }}
),
renamed as (
    select
        {{ adapter.quote("dispatching_base_num") }},
        {{ adapter.quote("pickup_datetime") }},
        {{ adapter.quote("drop_off_datetime") }},
        {{ adapter.quote("p_ulocation_id") }},
        {{ adapter.quote("d_olocation_id") }},
        {{ adapter.quote("sr_flag") }},
        {{ adapter.quote("affiliated_base_number") }}

    from source
)
select * from renamed
