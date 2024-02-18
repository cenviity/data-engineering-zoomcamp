# Modified from https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/be68361c402995a8057ab9f70e930f7c56c18ec9/03-data-warehouse/extras/web_to_gcs.py
import os

import pandas as pd
from google.cloud import storage

"""
Pre-reqs:
1. `pip install pandas pyarrow google-cloud-storage`
2. Set GOOGLE_APPLICATION_CREDENTIALS to your project/service-account key
3. Set GCP_GCS_BUCKET as your bucket or change default value of BUCKET
"""

init_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/"
# switch out the bucketname
BUCKET = os.environ.get("GCP_GCS_BUCKET", "de-zoomcamp-module-3-homework-vincent-yim")


def upload_to_gcs(bucket, object_name, local_file):
    """
    Ref: https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python
    """
    # # WORKAROUND to prevent timeout for files > 6 MB on 800 kbps upload speed.
    # # (Ref: https://github.com/googleapis/python-storage/issues/74)
    # storage.blob._MAX_MULTIPART_SIZE = 5 * 1024 * 1024  # 5 MB
    # storage.blob._DEFAULT_CHUNKSIZE = 5 * 1024 * 1024  # 5 MB

    client = storage.Client()
    bucket = client.bucket(bucket)
    blob = bucket.blob(object_name)
    blob.upload_from_filename(local_file)


def web_to_gcs(year, service):
    for i in range(12):

        # sets the month part of the file_name string
        month = "0" + str(i + 1)
        month = month[-2:]

        # Parquet file_name
        file_name = f"{service}_tripdata_{year}-{month}.parquet"

        # download it using requests via a pandas df
        request_url = f"{init_url}{file_name}"

        # read it back into a parquet file
        df = pd.read_parquet(request_url)
        df.to_parquet(file_name, engine="pyarrow")
        print(f"Parquet: {file_name}")

        # upload it to gcs
        upload_to_gcs(BUCKET, f"{service}/{file_name}", file_name)
        print(f"GCS: {service}/{file_name}")


web_to_gcs("2022", "green")
