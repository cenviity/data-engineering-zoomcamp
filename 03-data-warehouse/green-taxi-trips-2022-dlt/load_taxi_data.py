import dlt
from dlt.destinations import filesystem
from green_taxi_trips import taxi_trips


def main():
    for month in range(1, 13):
        load(month)


def load(month):
    pipeline = dlt.pipeline(
        pipeline_name="load_taxi_data",
        dataset_name="green_taxi_trips_2022",
    )

    destination = filesystem(
        layout=f"{{table_name}}/green_tripdata_2022-{month:02}",
    )

    load_info = pipeline.run(
        taxi_trips(month),
        destination=destination,
        loader_file_format="parquet",
        table_name="trips",
    )
    print(load_info)


if __name__ == "__main__":
    main()
