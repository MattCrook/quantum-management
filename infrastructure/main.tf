provider "google" {
  project = "quantum-management-295116"
  region  = "us-central1"
}

terraform {
  required_version = ">= 1.7.0"
  #    backend "remote" {
  #      bucket      = "tf-quantummanagement-state"
  #      prefix      = "infrastructure/bucket/terraform.tfstate"
  #  }
}
