terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.13.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials)
  project     = var.project
  region      = var.region
}

resource "google_bigquery_dataset" "ny_taxi_trips" {
  dataset_id = var.bq_dataset_name
  location   = var.location
}
