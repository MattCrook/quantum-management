/*
resource "google_app_engine_application" "quantum_management" {
  project     = "quantum-management-295116"
  location_id = "us-central"
}

# resource "google_app_engine_domain_mapping" "domain_mapping" {
#   domain_name = "verified-domain.com"
#   ssl_settings {
#     ssl_management_type = "AUTOMATIC"
#   }
# }


resource "google_storage_bucket" "tf_state" {
    project       = "quantum-management-295116"
    name          = "tf-quantummanagement-state"
    location      = "US"
    storage_class = "STANDARD"
    force_destroy = true

    versioning {
        enabled = true
    }
}



output "name" { value = google_app_engine_application.quantum_management.name }
output "url_dispatch_rule " { value = google_app_engine_application.quantum_management.url_dispatch_rule }
output "code_bucket " { value = google_app_engine_application.quantum_management.code_bucket }
output "default_hostname " { value = google_app_engine_application.quantum_management.default_hostname }
output "default_bucket  " { value = google_app_engine_application.quantum_management.default_bucket }
output "gcr_domain  " { value = google_app_engine_application.quantum_management.gcr_domain }
*/
