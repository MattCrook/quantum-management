# resource "google_compute_firewall" "ingress_allow_quantum_management_80" {
#   project   = var.project_id
#   network   = "default"
#   name      = "ingress-allow-quantum-management-default-port-80"
#   direction = "INGRESS"
#   priority  = 900

#   allow {
#     protocol = "tcp"
#     ports    = ["8080", "80",]
#   }

#   allow {
#     protocol = "udp"
#   }

#   allow {
#     protocol = "icmp"
#   }

#   source_ranges = []

#   target_tags = ["quantum-management"]

#   log_config {
#     metadata = "EXCLUDE_ALL_METADATA"
#   }
# }

# resource "google_compute_firewall" "ingress_deny_all_quantum_management" {
#   project   = var.project_id
#   network   = "default"
#   name      = "ingress-deny-all-quantum-management"
#   direction = "INGRESS"
#   priority  = 1001

#   deny {
#     protocol = "tcp"
#   }

#   deny {
#     protocol = "udp"
#   }

#   deny {
#     protocol = "icmp"
#   }

#   source_ranges = ["0.0.0.0/0"]
#   target_tags   = ["quantum-management"]

#   log_config {
#     metadata = "EXCLUDE_ALL_METADATA"
#   }
# }

resource "google_compute_firewall" "ingress_allow_quantum_management_healthcheck_and_iap" {
  project   = var.project_id
  network   = "default"
  name      = "ingress-allow-quantum-management-hc-and-iap-ranges"
  direction = "INGRESS"
  priority  = 900

  allow {
    protocol = "tcp"
    ports    = ["8080", "80", "443", "8000"]
  }

  source_ranges = ["35.235.240.0/20", "130.211.0.0/22", "35.191.0.0/16"]
  target_tags   = ["quantum-management"]

  log_config {
    metadata = "EXCLUDE_ALL_METADATA"
  }
}
