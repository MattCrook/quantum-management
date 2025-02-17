resource "google_compute_firewall" "ingress_allow_quantum_management_default_ports" {
  project   = var.project_id
  network   = "default"
  name      = "ingress-allow-quantum-management-default-ports"
  direction = "INGRESS"
  priority  = 100

  allow {
    protocol = "tcp"
    ports    = ["8080", "80", "443"]
  }

  allow {
    protocol = "udp"
  }

  allow {
    protocol = "icmp"
  }

  source_ranges = ["34.85.150.7/32", "68.84.85.238/32"]
  target_tags   = ["quantum-management"]

  log_config {
    metadata = "EXCLUDE_ALL_METADATA"
  }
}

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
  priority  = 1000

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

resource "google_compute_firewall" "ingress_allow_ssh_quantum_management" {
  name      = "ingress-allow-ssh-quantum-management"
  project   = var.project_id
  network   = "default"
  direction = "INGRESS"
  priority  = 1000

  allow {
    protocol = "tcp"
    ports    = ["22"]
  }

  source_ranges = ["66.84.85.238/32", "34.85.150.7/32"]
  target_tags   = ["allow-quantum-ssh"]


  log_config {
    metadata = "EXCLUDE_ALL_METADATA"
  }
}

resource "google_compute_firewall" "egress_allow_all" {
  name      = "egress-allow-all"
  project   = var.project_id
  network   = "default"
  direction = "EGRESS"

  allow {
    protocol = "all"
  }

  destination_ranges = ["0.0.0.0/0"]
  target_tags        = ["quantum-management"]

}
