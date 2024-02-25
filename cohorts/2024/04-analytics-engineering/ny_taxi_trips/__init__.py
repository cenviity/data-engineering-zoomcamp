import io
from collections.abc import Iterator

import dlt
import pandas as pd
from pandas import DataFrame
from requests_cache import CachedSession

from .settings import URL


def taxi_trips(
    category: str, year: int, month: int, session: CachedSession
) -> Iterator[DataFrame]:
    url = URL.format(category=category, year=year, month=month)
    response = session.get(url)
    response.raise_for_status()

    df = pd.read_parquet(io.BytesIO(response.content))
    # Cast to nullable data types
    # So that a column with both ints and nulls is not treated as floats
    yield df.convert_dtypes()


@dlt.source
def source(year, month, session: CachedSession):
    for category in ["yellow", "green", "fhv"]:
        yield dlt.resource(
            taxi_trips(category, year, month, session),
            name=f"{category}_taxi_trips",
        )
