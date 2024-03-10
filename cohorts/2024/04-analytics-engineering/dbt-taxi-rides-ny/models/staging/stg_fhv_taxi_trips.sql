{{
    config(
        materialized="view"
    )
}}

with

tripdata as (

    select
        *,
        row_number() over (partition by dispatching_base_num, pickup_datetime) as rn

    from {{ source("staging", "fhv_taxi_trips") }}

    where dispatching_base_num is not null

)

select
    -- identifiers
    {{ dbt_utils.generate_surrogate_key(["dispatching_base_num", "pickup_datetime"]) }} as tripid,
    {{ dbt.safe_cast("dispatching_base_num", api.Column.translate_type("integer")) }} as dispatching_base_number,
    {{ dbt.safe_cast("p_ulocation_id", api.Column.translate_type("integer")) }} as pickup_locationid,
    {{ dbt.safe_cast("d_olocation_id", api.Column.translate_type("integer")) }} as dropoff_locationid,
    {{ dbt.safe_cast("sr_flag", api.Column.translate_type("integer")) }} as shared_ride_flag,
    {{ dbt.safe_cast("affiliated_base_number", api.Column.translate_type("integer")) }} as affiliated_base_number,

    -- timestamps
    cast(pickup_datetime as timestamp) as pickup_datetime,
    cast(drop_off_datetime as timestamp) as dropoff_datetime,

from tripdata

where rn = 1

-- dbt build --select <model_name> --vars '{'is_test_run': 'false'}'
{% if var("is_test_run", default=true) %}

    limit 100

{% endif %}
