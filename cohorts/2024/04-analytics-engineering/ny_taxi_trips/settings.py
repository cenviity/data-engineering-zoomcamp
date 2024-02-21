"""Pipeline settings and constants"""

URL = (
    "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/"
    "{category}/{category}_tripdata_{year}-{month:02}.csv.gz"
)
CATEGORIES = ["yellow", "green", "fhv"]
YEARS = [2019, 2020]
MONTHS = range(1, 13)
