import pandas as pd

if "data_loader" not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if "test" not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    dtypes = {
        "VendorID": pd.Int64Dtype(),
        "store_and_fwd_flag": str,
        "RatecodeID": pd.Int64Dtype(),
        "PULocationID": pd.Int64Dtype(),
        "DOLocationID": pd.Int64Dtype(),
        "passenger_count": pd.Int64Dtype(),
        "trip_distance": float,
        "fare_amount": float,
        "extra": float,
        "mta_tax": float,
        "tip_amount": float,
        "tolls_amount": float,
        "ehail_fee": float,
        "improvement_surcharge": float,
        "total_amount": float,
        "payment_type": pd.Int64Dtype(),
        "trip_type": pd.Int64Dtype(),
        "congestion_surcharge": float,
    }

    datetime_cols = ["lpep_pickup_datetime", "lpep_dropoff_datetime"]

    def get_trips_data(year, month):
        url = f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_{year}-{month}.csv.gz"
        return pd.read_csv(url, dtype=dtypes, parse_dates=datetime_cols)

    month_data = (get_trips_data(2020, month) for month in range(10, 13))
    df = pd.concat(month_data)

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, "The output is undefined"
