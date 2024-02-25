import itertools

import dlt
from ny_taxi_trips import source
from ny_taxi_trips.settings import MONTHS, YEARS

pipeline = dlt.pipeline(
    pipeline_name="ny_taxi_trips",
    destination="bigquery",
    import_schema_path="schemas/import",
    export_schema_path="schemas/export",
    progress="enlighten",
)


def load(category: str, year: int, month: int, write_disposition: str = "append"):
    resource = f"{category}_taxi_trips"
    load_info = pipeline.run(
        source(year, month).with_resources(resource),
        loader_file_format="parquet",
        dataset_name="ny_taxi_trips",
        table_name=resource,
        write_disposition=write_disposition,
    )
    print(load_info)


if __name__ == "__main__":
    # Load trip data for yellow and green taxis in 2019 and 2020
    for product in itertools.product(["yellow", "green"], YEARS, MONTHS):
        load(**dict(zip(("category", "year", "month"), product)))

    # Load trip data for FHV (for-hire vehicles) in 2019
    for month in MONTHS:
        load(category="fhv", year=2019, month=month)
