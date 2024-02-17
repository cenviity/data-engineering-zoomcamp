import io

import dlt
import pandas as pd
from dlt.sources.helpers import requests


@dlt.resource
def taxi_trips(month):
    url = (
        "https://d37ci6vzurychx.cloudfront.net/trip-data/"
        f"green_tripdata_2022-{month:02}.parquet"
    )
    response = requests.get(url, stream=True)
    response.raise_for_status()
    yield pd.read_parquet(io.BytesIO(response.content))
