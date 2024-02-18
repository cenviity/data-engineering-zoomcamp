variable "credentials" {
  description = "My credentials"
  default     = "personal-gcp.json"
}

variable "project_id" {
  type        = string
  description = "The name of the project"
  default     = "even-ally-412601"
}

variable "region" {
  type        = string
  description = "The default compute region"
  default     = "us-west2"
}

variable "zone" {
  type        = string
  description = "The default compute zone"
  default     = "us-west2-a"
}
