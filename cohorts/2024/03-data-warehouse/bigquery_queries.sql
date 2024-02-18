-- Create external table from Parquet files loaded into GCS bucket
create or replace external table even-ally-412601.green_taxi_trips_2022.trips_external
options (
  format = 'parquet',
  uris = ['gs://de-zoomcamp-module-3-homework-vincent-yim/green/green_tripdata_2022-*.parquet']
);

-- Create materialised table from external table
create or replace table even-ally-412601.green_taxi_trips_2022.trips as (
  select *
  from even-ally-412601.green_taxi_trips_2022.trips_external
);

-- Q1
select count(*) as row_count
from even-ally-412601.green_taxi_trips_2022.trips;
-- RESULT:
-- row_count
-- 840402

-- Q2
-- Estimated 0 B
select distinct(PULocationID)
from even-ally-412601.green_taxi_trips_2022.trips_external;

-- Estimated 6.41 MB
select distinct(PULocationID)
from even-ally-412601.green_taxi_trips_2022.trips;

-- Q3
select count(*) as records_with_zero_fare
from even-ally-412601.green_taxi_trips_2022.trips
where fare_amount = 0;
-- RESULT:
-- records_with_zero_fare
-- 1622

-- Q4
create or replace table even-ally-412601.green_taxi_trips_2022.trips_partitioned
partition by date(lpep_pickup_datetime)
cluster by PULocationID as (
  select *
  from even-ally-412601.green_taxi_trips_2022.trips
);

-- Q5
-- Estimated 12.82 MB
select distinct(PULocationID)
from even-ally-412601.green_taxi_trips_2022.trips
where date(lpep_pickup_datetime) between '2022-06-01' and '2022-06-30';

-- Estimated 1.12 MB
select distinct(PULocationID)
from even-ally-412601.green_taxi_trips_2022.trips_partitioned
where date(lpep_pickup_datetime) between '2022-06-01' and '2022-06-30';

-- Q8
-- Estimate 0 B
select count(*) as row_count
from even-ally-412601.green_taxi_trips_2022.trips;
