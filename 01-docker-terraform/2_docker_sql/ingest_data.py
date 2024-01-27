#!/usr/bin/env python
# coding: utf-8

import argparse
import os
from time import time

import pandas as pd
from sqlalchemy import create_engine


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    if url.endswith(".csv.gz"):
        csv_name = "output.csv.gz"
    else:
        csv_name = "output.csv"

    os.system(f"wget {url} -O {csv_name}")

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    df = next(df_iter)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.head(n=0).to_sql(name=table_name, con=engine, if_exists="replace")

    df.to_sql(name=table_name, con=engine, if_exists="append")

    while True:
        t_start = time()

        df = next(df_iter)

        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

        df.to_sql(name=table_name, con=engine, if_exists="append")

        t_end = time()

        print(f"Inserted another chunk... Took {(t_end - t_start):.3f} seconds")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest CSV data into Postgres")
    parser.add_argument("--user", help="username for Postgres")
    parser.add_argument("--password", help="password for Postgres")
    parser.add_argument("--host", help="host for Postgres")
    parser.add_argument("--port", help="port for Postgres")
    parser.add_argument("--db", help="database name for Postgres")
    parser.add_argument(
        "--table_name", help="name of the table to write the results to"
    )
    parser.add_argument("--url", help="URL of the CSV file")

    args = parser.parse_args()

    main(args)
