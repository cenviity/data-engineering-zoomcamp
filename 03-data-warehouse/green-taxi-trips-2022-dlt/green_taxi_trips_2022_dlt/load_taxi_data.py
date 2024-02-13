import io

import dlt
import pandas as pd
from dlt.sources.helpers import requests

url = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-01.parquet"

response = requests.get(url, stream=True)
response.raise_for_status()

pipeline = dlt.pipeline(
    pipeline_name="load_taxi_data",
    destination="duckdb",
    dataset_name="green_taxi_trips_2022",
)

load_info = pipeline.run(
    pd.read_parquet(io.BytesIO(response.content)),
    loader_file_format="parquet",
    table_name="trips",
    write_disposition="replace",
)

print(load_info)
