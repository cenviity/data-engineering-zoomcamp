provider "google" {
  project     = var.project_id
  region      = var.region
  zone        = var.zone
  credentials = var.credentials
}

resource "google_storage_bucket" "de-zoomcamp-module-2-homework" {
  name                        = "de-zoomcamp-module-2-homework-vincent-yim"
  location                    = "US"
  storage_class               = "STANDARD"
  public_access_prevention    = "enforced"
  uniform_bucket_level_access = true
}
