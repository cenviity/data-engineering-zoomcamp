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
    output = []
    for i in range(1, 13):
        url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-{i:02}.parquet"
        print(f"Loaded month {i}: {url}")
        output.append({"month": i, "data": pd.read_parquet(url)})

    return output


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, "The output is undefined"
