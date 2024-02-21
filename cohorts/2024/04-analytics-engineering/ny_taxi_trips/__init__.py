import io
import itertools
import logging
from collections.abc import Iterator

import dlt
import pandas as pd
import requests
from dlt.sources import DltResource
from pandas import DataFrame

from .settings import CATEGORIES, MONTHS, URL, YEARS


def taxi_trips(category, year, month) -> Iterator[DataFrame]:
    url = URL.format(category=category, year=year, month=month)
    logging.info(
        "Loading CSV: category [%s] year [%d] month [%d]",
        category,
        year,
        month,
    )
    # url = URL.format(dict(zip(["category", "year", "month"], args)))
    response = requests.get(url, stream=True)
    response.raise_for_status()
    yield pd.read_csv(io.BytesIO(response.content), compression="gzip")
    # yield pd.read_csv(url)


def create_resource(category, year, month):
    logging.info(
        "Creating resource: category [%s] year [%d] month [%d]",
        category,
        year,
        month,
    )
    return dlt.resource(
        taxi_trips(category, year, month),
        name="_".join(map(str, [category, year, month])),
        table_name="ny_taxi_trips",
        write_disposition="replace",
    )


@dlt.source
def source() -> Iterator[DltResource]:
    yield from (
        create_resource(*cmb) for cmb in itertools.product(CATEGORIES, YEARS, MONTHS)
    )
