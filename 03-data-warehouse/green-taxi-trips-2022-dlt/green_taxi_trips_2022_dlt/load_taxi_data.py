import io

import dlt
import pandas as pd
from dlt.destinations import filesystem
from dlt.sources.helpers import requests

pipeline = dlt.pipeline(
    pipeline_name="load_taxi_data",
    dataset_name="green_taxi_trips_2022",
)

for month in range(1, 13):
    _month = f"{month:02}"

    @dlt.resource
    def load_parquet_files():
        url = (
            "https://d37ci6vzurychx.cloudfront.net/trip-data/"
            f"green_tripdata_2022-{_month}.parquet"
        )
        response = requests.get(url, stream=True)
        response.raise_for_status()
        data = pd.read_parquet(io.BytesIO(response.content))
        yield data

    destination = filesystem(
        layout=f"{{table_name}}/green_tripdata_2022-{_month}",
    )

    load_info = pipeline.run(
        load_parquet_files,
        destination=destination,
        loader_file_format="parquet",
        table_name="trips",
    )
    print(load_info)
