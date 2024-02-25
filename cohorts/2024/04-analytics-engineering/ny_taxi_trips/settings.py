"""Pipeline settings and constants"""

URL = (
    "https://d37ci6vzurychx.cloudfront.net/trip-data/"
    "{category}_tripdata_{year}-{month:02}.parquet"
)
CATEGORIES = ["yellow", "green", "fhv"]
YEARS = [2019, 2020]
MONTHS = range(1, 13)
