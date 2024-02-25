variable "credentials" {
  description = "My credentials"
  default     = "./keys/even-ally-412601-bd776a8a9c22.json"
}

variable "project" {
  description = "Project"
  default     = "even-ally-412601"
}

variable "region" {
  description = "Region"
  default     = "us-central1"
}

variable "location" {
  description = "Project location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery dataset name"
  default     = "ny_taxi_trips"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket name"
  default     = "de-zoomcamp-vincent-yim"
}

variable "gcs_storage_class" {
  description = "Bucket Storage class"
  default     = "STANDARD"
}
