resource "google_compute_address" "quantum_management" {
  project       = var.project_id
  region        = var.region
  name          = "quantum-management"
  address_type  = "EXTERNAL"
  network_tier  = "PREMIUM"
  ip_version    = "IPV4"
}

resource "google_compute_forwarding_rule" "quantum_management" {
  project               = var.project_id
  region                = var.region
  name                  = "qm-external-l4-network-lb"
  ip_protocol           = "TCP"
  load_balancing_scheme = "EXTERNAL"
  port_range            = "80"
  target                = google_compute_target_pool.quantum_management.id
  ip_address            = google_compute_address.quantum_management.address
}

resource "google_compute_target_pool" "quantum_management" {
  project          = var.project_id
  region           = var.region
  name             = "qm-external-l4-network-lb"
  session_affinity = "CLIENT_IP"
  instances        = [google_compute_instance.quantum_management.self_link]
  # security_policy = google_compute_security_policy.cloudarmor_tcp_proxy_backends.id    # beta

  health_checks = [
    google_compute_http_health_check.legacy_tcp_80.name
  ]
}

resource "google_compute_http_health_check" "legacy_tcp_80" {
  project = var.project_id
  name    = "tcp-80-target-pool-health-check"
  port    = 80

  check_interval_sec  = 25
  healthy_threshold   = 1
  timeout_sec         = 10
  unhealthy_threshold = 5
}






resource "google_compute_forwarding_rule" "quantum_management_healthcheck" {
  project               = var.project_id
  region                = var.region
  name                  = "qm-external-l4-network-lb-healthcheck"
  ip_protocol           = "TCP"
  load_balancing_scheme = "EXTERNAL"
  port_range            = "8080"
  target                = google_compute_target_pool.quantum_management_healthcheck.id
  ip_address            = google_compute_address.quantum_management.address
}

resource "google_compute_target_pool" "quantum_management_healthcheck" {
  project          = var.project_id
  region           = var.region
  name             = "qm-external-l4-network-lb-healthcheck"
  session_affinity = "CLIENT_IP"
  instances        = [google_compute_instance.quantum_management.self_link]
  # security_policy = google_compute_security_policy.cloudarmor_tcp_proxy_backends.id    # beta

  health_checks = [
    google_compute_http_health_check.legacy_tcp_healthcheck_8080.name
  ]
}


resource "google_compute_http_health_check" "legacy_tcp_healthcheck_8080" {
  project = var.project_id
  name    = "tcp-8080-target-pool-health-check"
  port    = 8080

  check_interval_sec  = 25
  healthy_threshold   = 1
  timeout_sec         = 10
  unhealthy_threshold = 5
}
