provider "google" {
  project     = "quantum-management-295116"
  region      = "us-central1"
  zone        = "us-central1-a"
  credentials = "./google_sa_account.json"
}

terraform {
  required_version = ">= 1.7.0"
  #    backend "remote" {
  #      bucket      = "tf-quantummanagement-state"
  #      prefix      = "infrastructure/bucket/terraform.tfstate"
  #  }
}


data "google_compute_subnetwork" "usc1_default_subnet" {
  project = var.project_id
  name    = "default"
  region  = "us-central1"
}

# data "google_project" "project" {
# }


resource "random_id" "random_role_id_suffix" {
  byte_length = 2
}

output "vm_network_ip" {
  value = google_compute_instance.quantum_management.network_interface.0.network_ip
}

output "l4_network_lb_ip" {
  value = google_compute_forwarding_rule.quantum_management.ip_address
}

# output "tcp_proxy_lb_ip" {
#   value = google_compute_global_forwarding_rule.tcp_proxy.ip_address
# }





# output "name" { value = google_app_engine_application.quantum_management.name }
# output "url_dispatch_rule " { value = google_app_engine_application.quantum_management.url_dispatch_rule }
# output "code_bucket " { value = google_app_engine_application.quantum_management.code_bucket }
# output "default_hostname " { value = google_app_engine_application.quantum_management.default_hostname }
# output "default_bucket  " { value = google_app_engine_application.quantum_management.default_bucket }
# output "gcr_domain  " { value = google_app_engine_application.quantum_management.gcr_domain }
