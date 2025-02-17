/*
resource "google_compute_security_policy" "cloudarmor_tcp_proxy_backends" {
  project = var.project_id
  name    = "cloudarmor-tcp-proxy-security-policy"

  rule {
    action   = "allow"
    priority = "1000"
    match {
      versioned_expr = "SRC_IPS_V1"
      config {
        src_ip_ranges = [
          "35.235.240.0/20", # IAP CIDR
          "130.211.0.0/22",  # Healthcheck CIDR
          "35.191.0.0/16",   # Healthcheck CIDR
        ]
      }
    }
    description = "IAP IPs | HealthCheck CIDR Ranges"
  }


  rule {
    action   = "deny(403)"
    priority = "2147483647"
    match {
      versioned_expr = "SRC_IPS_V1"
      config {
        src_ip_ranges = ["*"]
      }
    }
    description = "default rule"
  }
}
*/
