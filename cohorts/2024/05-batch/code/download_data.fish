set TAXI_TYPE $argv[1] # yellow
set YEAR $argv[2] # 2020
set URL_PREFIX "https://github.com/DataTalksClub/nyc-tlc-data/releases/download"

for MONTH in (seq 1 12)
    set FMONTH (printf %02d $MONTH)
    set URL {$URL_PREFIX}/{$TAXI_TYPE}/{$TAXI_TYPE}_tripdata_{$YEAR}-{$FMONTH}.csv.gz

    set LOCAL_PREFIX data/raw/{$TAXI_TYPE}/{$YEAR}/{$FMONTH}
    set LOCAL_FILE {$TAXI_TYPE}_tripdata_{$YEAR}_{$FMONTH}.csv.gz
    set LOCAL_PATH {$LOCAL_PREFIX}/{$LOCAL_FILE}

    echo "Downloading $URL to $LOCAL_PATH"
    mkdir -p $LOCAL_PREFIX
    curl -L $URL -o $LOCAL_PATH
end
