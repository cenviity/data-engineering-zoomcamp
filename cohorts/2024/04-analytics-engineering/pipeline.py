import dlt
from ny_taxi_trips import source
from ny_taxi_trips.settings import CATEGORIES, MONTHS, YEARS


def load(resources: list[str]) -> None:
    pipeline = dlt.pipeline(
        pipeline_name="ny_taxi_trips",
        destination="bigquery",
        progress="enlighten",
    )
    load_info = pipeline.run(
        source().with_resources(*resources),
        loader_file_format="parquet",
        dataset_name="ny_taxi_trips",
    )
    print(load_info)


if __name__ == "__main__":
    resources = [
        "_".join(map(str, [category, year, month]))
        for category in CATEGORIES
        for year in YEARS
        for month in MONTHS
    ]
    load(resources)
