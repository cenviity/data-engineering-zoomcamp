import io
import logging

import dlt
import pandas as pd
from dlt.destinations import filesystem
from dlt.sources.credentials import GcpServiceAccountCredentials
from dlt.sources.helpers import requests

logging_level = logging.INFO
logging.basicConfig(level=logging_level)

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

    credentials = GcpServiceAccountCredentials()
    with open(".dlt/gcp-secrets.json", "r") as f:
        native_value = f.read()
    credentials.parse_native_representation(native_value)

    destination = filesystem(
        bucket_url="gs://de-zoomcamp-module-3-homework-vincent-yim-dlt",
        credentials=credentials,
        layout=f"{{table_name}}/green_tripdata_2022-{_month}",
    )

    pipeline = dlt.pipeline(
        pipeline_name="load_taxi_data",
        destination=destination,
        dataset_name="green_taxi_trips_2022",
    )

    load_info = pipeline.run(
        load_parquet_files,
        loader_file_format="parquet",
        table_name="trips",
    )
    logging.info(load_info)
