import itertools

import dlt
from ny_taxi_trips import taxi_trips
from ny_taxi_trips.settings import MONTHS, YEARS


def load(category: str, year: int, month: int):
    pipeline = dlt.pipeline(
        pipeline_name="ny_taxi_trips",
        destination="bigquery",
        progress="enlighten",
    )
    load_info = pipeline.run(
        taxi_trips(category, year, month),
        loader_file_format="parquet",
        dataset_name="ny_taxi_trips",
        table_name=f"{category}_taxi_trips",
    )
    print(load_info)


if __name__ == "__main__":
    # Load trip data for yellow and green taxis in 2019 and 2020
    for product in itertools.product(["yellow", "green"], YEARS, MONTHS):
        load(**dict(zip(("category", "year", "month"), product)))

    # Load trip data for FHV (for-hire vehicles) in 2019
    for month in MONTHS:
        load(category="fhv", year=2019, month=month)
