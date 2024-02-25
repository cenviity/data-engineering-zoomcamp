import itertools

import dlt
import requests_cache
from ny_taxi_trips import source
from ny_taxi_trips.settings import MONTHS, YEARS

pipeline = dlt.pipeline(
    pipeline_name="ny_taxi_trips",
    destination="bigquery",
    import_schema_path="schemas/import",
    # export_schema_path="schemas/export",
    progress="enlighten",
)


def load(
    category: str,
    year: int,
    month: int,
    columns: dict[str, dict[str, str]],
    write_disposition: str = "append",
):
    session = requests_cache.CachedSession()
    resource = f"{category}_taxi_trips"
    load_info = pipeline.run(
        source(year, month, session=session).with_resources(resource),
        loader_file_format="parquet",
        dataset_name="ny_taxi_trips",
        table_name=resource,
        columns=columns,
        write_disposition=write_disposition,
    )
    print(load_info)


if __name__ == "__main__":
    # Load trip data for yellow and green taxis in 2019 and 2020
    for product in itertools.product(["yellow", "green"], YEARS, MONTHS):
        load(
            **dict(zip(("category", "year", "month"), product)),
            columns={
                "vendor_id": {"data_type": "bigint"},
                "passenger_count": {"data_type": "bigint"},
                "ratecode_id": {"data_type": "bigint"},
                "pu_location_id": {"data_type": "bigint"},
                "do_location_id": {"data_type": "bigint"},
                "payment_type": {"data_type": "bigint"},
            },
        )

    # Load trip data for FHV (for-hire vehicles) in 2019
    for month in MONTHS:
        load(
            category="fhv",
            year=2019,
            month=month,
            columns={
                "p_ulocation_id": {"data_type": "bigint"},
                "d_olocation_id": {"data_type": "bigint"},
                "sr_flag": {"data_type": "bigint"},
            },
        )
