resource "google_compute_global_forwarding_rule" "tcp_proxy" {
  provider              = google-beta
  project               = var.project_id
  name                  = "tcp-proxy-lb"
  ip_protocol           = "TCP"
  load_balancing_scheme = "EXTERNAL"
  port_range            = 80
  target                = google_compute_target_tcp_proxy.tcp_proxy.self_link
  labels                = { application = "quantum-management" }
}

resource "google_compute_target_tcp_proxy" "tcp_proxy" {
  provider        = google-beta
  project         = var.project_id
  name            = "tcp-proxy-lb-target-proxy"
  backend_service = google_compute_backend_service.tcp_proxy.id
}

resource "google_compute_backend_service" "tcp_proxy" {
  provider                        = google-beta
  project                         = var.project_id
  name                            = "tcp-proxy-lb-backend-service"
  protocol                        = "TCP"
  timeout_sec                     = 10
  connection_draining_timeout_sec = 10
  load_balancing_scheme           = "EXTERNAL"
  session_affinity                = "CLIENT_IP"
  health_checks                   = [google_compute_health_check.tcp_8060.id]
  # security_policy                 = google_compute_security_policy.cloudarmor_tcp_proxy_backends.id
  backend {
    balancing_mode        = "RATE"
    max_rate_per_endpoint = 1000
    group                 = google_compute_network_endpoint_group.quantummanagement.id
  }

  log_config {
    enable      = true
    sample_rate = 1.0
  }
}

resource "google_compute_network_endpoint_group" "quantummanagement" {
  provider              = google-beta
  project               = var.project_id
  name                  = "tcp-proxy-lb-neg-group"
  zone                  = var.zone
  network               = "default"
  subnetwork            = data.google_compute_subnetwork.usc1_default_subnet.id
  network_endpoint_type = "GCE_VM_IP_PORT"
  default_port          = "80"
}

resource "google_compute_network_endpoint" "quantummanagement" {
  project                = var.project_id
  zone                   = google_compute_network_endpoint_group.quantummanagement.zone
  network_endpoint_group = google_compute_network_endpoint_group.quantummanagement.name
  instance               = data.google_compute_instance.quantummanagement.name
  port                   = google_compute_network_endpoint_group.quantummanagement.default_port
  ip_address             = data.google_compute_instance.quantummanagement.network_interface.0.network_ip
}


resource "google_compute_health_check" "tcp_proxy_lb" {
  project = var.project_id
  name    = "tcp-proxy-lb-health-check-80"

  check_interval_sec  = 25
  healthy_threshold   = 1
  timeout_sec         = 10
  unhealthy_threshold = 5

  tcp_health_check {
    port = "80"
  }
}
