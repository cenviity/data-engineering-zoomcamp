## Module 1 Homework

## Docker & SQL

In this homework we'll prepare the environment
and practice with Docker and SQL


## Question 1. Knowing docker tags

Run the command to get information on Docker

```docker --help```

Now run the command to get help on the "docker build" command:

```docker build --help```

Do the same for "docker run".

Which tag has the following text? - *Automatically remove the container when it exits*

- `--delete`
- `--rc`
- `--rmc`
- `--rm`

### 🔵 Answer

<details>
    <summary>Show / hide</summary>

```bash
$ docker run --help

Usage:  docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

Create and run a new container from an image

Aliases:
  docker container run, docker run

Options:
      --add-host list                    Add a custom host-to-IP mapping (host:ip)
      --annotation map                   Add an annotation to the container (passed through to the OCI runtime) (default map[])
  -a, --attach list                      Attach to STDIN, STDOUT or STDERR
[...]
      --rm                               Automatically remove the container when it exits
[...]
```

The answer is `--rm`.
</details>


## Question 2. Understanding docker first run

Run docker with the python:3.9 image in an interactive mode and the entrypoint of bash.
Now check the python modules that are installed ( use ```pip list``` ).

What is version of the package *wheel* ?

- 0.42.0
- 1.0.0
- 23.0.1
- 58.1.0

### 🔵 Answer

<details>
    <summary>Show / hide</summary>

```bash
$ docker run -it --entrypoint=bash python:3.9

root@6664d9488f9d:/# pip list
Package    Version
---------- -------
pip        23.0.1
setuptools 58.1.0
wheel      0.42.0
```

The version of the package *wheel* is `0.42.0`.
</details>


# Prepare Postgres

Run Postgres and load data as shown in the videos
We'll use the green taxi trips from September 2019:

```wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz```

You will also need the dataset with zones:

```wget https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv```

Download this data and put it into Postgres (with jupyter notebooks or with a pipeline)


## 🔵 Ingesting data

<details>
    <summary>Show / hide</summary>

Update `ingest_data.py` to handle different column names in green taxi trips data (see commit 5272f83cc483f648ffeb0f50798f65b2cf89c26e).

Rebuild the image:

```bash
docker build -t taxi_ingest:v001 .
```

Start up containers:

```bash
$ docker compose up -d
```

Run ingest script to load green taxi trips data into database:

```bash
$ docker run -it \
    --network=2_docker_sql_default \
    taxi_ingest:v001 \
    --user=root \
    --password=root \
    --host=pgdatabase \
    --port=5432 \
    --db=ny_taxi \
    --table_name=green_taxi_trips \
    --url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz"
```

Taxi zones data has already been loaded earlier in commit 7bca57edefe45c869522352759e76b93f2e578d8.
</details>


## Question 3. Count records

How many taxi trips were totally made on September 18th 2019?

Tip: started and finished on 2019-09-18.

Remember that `lpep_pickup_datetime` and `lpep_dropoff_datetime` columns are in the format timestamp (date and hour+min+sec) and not in date.

- 15767
- 15612
- 15859
- 89009

### 🔵 Answer

<details>
    <summary>Show / hide</summary>

[SQL query](question3.sql)

Result:

```
"pickup_date"	"dropoff_date"	"count"
"2019-09-18"	"2019-09-18"	15612
```

The answer is **15612**.
</details>


## Question 4. Largest trip for each day

Which was the pick up day with the largest trip distance
Use the pick up time for your calculations.

- 2019-09-18
- 2019-09-16
- 2019-09-26
- 2019-09-21

### 🔵 Answer

<details>
    <summary>Show / hide</summary>

[SQL query](question4.sql)

Result:

```
"pickup_date"	"max"
"2019-09-26"	341.64
```

The answer is **2019-09-26**.
</details>


## Question 5. Three biggest pick up Boroughs

Consider lpep_pickup_datetime in '2019-09-18' and ignoring Borough has Unknown

Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?

- "Brooklyn" "Manhattan" "Queens"
- "Bronx" "Brooklyn" "Manhattan"
- "Bronx" "Manhattan" "Queens"
- "Brooklyn" "Queens" "Staten Island"

### 🔵 Answer

<details>
    <summary>Show / hide</summary>

[SQL query](question5.sql)

Result:

```
"pickup_date"	"borough"	"total_amount"
"2019-09-18"	"Brooklyn"	96333.24000000046
"2019-09-18"	"Manhattan"	92271.30000000083
"2019-09-18"	"Queens"	78671.71000000004
```

The answer is **"Brooklyn" "Manhattan" "Queens"**.
</details>


## Question 6. Largest tip

For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip?
We want the name of the zone, not the id.

Note: it's not a typo, it's `tip` , not `trip`

- Central Park
- Jamaica
- JFK Airport
- Long Island City/Queens Plaza

### 🔵 Answer

<details>
    <summary>Show / hide</summary>

[SQL query](question6.sql)

Result:

```
"dropoff_zone"	"tip_amount"
"JFK Airport"	62.31
```

The answer is **JFK Airport**.
</details>


## Terraform

In this section homework we'll prepare the environment by creating resources in GCP with Terraform.

In your VM on GCP/Laptop/GitHub Codespace install Terraform.
Copy the files from the course repo
[here](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform/1_terraform_gcp/terraform) to your VM/Laptop/GitHub Codespace.

Modify the files as necessary to create a GCP Bucket and Big Query Dataset.


## Question 7. Creating Resources

After updating the main.tf and variable.tf files run:

```
terraform apply
```

Paste the output of this command into the homework submission form.

### 🔵 Answer

<details>
    <summary>Show / hide</summary>

[Command line output](question7.txt)
</details>


## Submitting the solutions

* Form for submitting: https://courses.datatalks.club/de-zoomcamp-2024/homework/hw01
* You can submit your homework multiple times. In this case, only the last submission will be used.

Deadline: 29 January, 23:00 CET
