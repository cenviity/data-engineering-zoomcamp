import io
from collections.abc import Iterator

import dlt
import pandas as pd
from dlt.sources.helpers import requests
from pandas import DataFrame

from .settings import URL


def taxi_trips(category: str, year: int, month: int) -> Iterator[DataFrame]:
    url = URL.format(category=category, year=year, month=month)
    response = requests.get(url)
    response.raise_for_status()

    yield pd.read_parquet(io.BytesIO(response.content))


@dlt.source
def source(year, month):
    for category in ["yellow", "green", "fhv"]:
        yield dlt.resource(
            taxi_trips(category, year, month),
            name=f"{category}_taxi_trips",
        )
