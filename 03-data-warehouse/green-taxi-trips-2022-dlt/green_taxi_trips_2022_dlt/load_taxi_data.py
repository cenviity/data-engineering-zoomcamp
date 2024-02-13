import io

import dlt
import pandas as pd
from dlt.sources.helpers import requests


@dlt.resource
def load_parquet_files():
    for month in range(1, 13):
        url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-{month:02}.parquet"
        response = requests.get(url, stream=True)
        response.raise_for_status()
        data = pd.read_parquet(io.BytesIO(response.content))
        yield data


pipeline = dlt.pipeline(
    pipeline_name="load_taxi_data",
    destination="duckdb",
    dataset_name="green_taxi_trips_2022",
)

load_info = pipeline.run(
    load_parquet_files(),
    loader_file_format="parquet",
    table_name="trips",
    write_disposition="replace",
)

print(load_info)
