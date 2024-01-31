variable "credentials" {
  description = "My credentials"
  default     = "./keys/my-creds.json"
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
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket name"
  default     = "even-ally-412601-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage class"
  default     = "STANDARD"
}
