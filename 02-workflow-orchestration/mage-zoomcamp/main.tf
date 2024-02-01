terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials)

  project = "even-ally-412601"
  region  = "us-central1"
  zone    = "us-central1-c"
}

resource "google_storage_bucket" "mage-zoomcamp" {
  name                        = "mage-zoomcamp-vincent-yim"
  location                    = "US"
  storage_class               = "STANDARD"
  public_access_prevention    = "enforced"
  uniform_bucket_level_access = true
}
