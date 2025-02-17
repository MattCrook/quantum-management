#----------------------------------------#
# Creating:
# - Host Shared VPC Project
# - VPC network
# - Us-Central1 Subnet
# - Cloud Router Us-Central1
# - (Cloud Router NAT) NAT Instance
# - Static IPs (2) for NAT
#----------------------------------------#


/*
# resource "google_compute_shared_vpc_host_project" "quantum_management" {
#   project = "quantum-management-295116"
# }

resource "google_compute_network" "quantum_management" {
  name                    = "quantum-management-host"
  project                 = "quantum-management-295116"
  auto_create_subnetworks = false
  routing_mode            = "GLOBAL"
}

resource "google_compute_subnetwork" "us_cen1_infra" {
  name          = "us-cen1-infra"
  network       = google_compute_network.quantum_management.id
  ip_cidr_range = "10.0.0.0/16"
  region        = "us-central1"
}

module "cloud_router_us_central1" {
  source  = "terraform-google-modules/cloud-router/google"
  version = "~> 6.0"

  name    = "us-central1-router"
  project = var.project_id
  region  = "us-central1"
  network = google_compute_network.us_cen1_infra.id
}

resource "google_compute_address" "nat_address" {
  count  = 2
  name   = "nat-manual-ip-${count.index}"
  region = "us-central1"
}

resource "google_compute_router_nat" "prd_us_central_nat" {
  name   = "us_central1_router_nat"
  router = "us-central1-router"
  region = "us-central1"

  nat_ip_allocate_option              = "MANUAL_ONLY"
  nat_ips                             = google_compute_address.nat_address.*.self_link
  source_subnetwork_ip_ranges_to_nat  = "LIST_OF_SUBNETWORKS"
  subnetwork {
    name                    = google_compute_subnetwork.us_cen1_infra.id
    source_ip_ranges_to_nat = ["ALL_IP_RANGES"]
  }

  #enable_endpoint_independent_mapping = false
  #min_ports_per_vm = 1024
  ###enable_dynamic_port_allocation        = true
  ###max_ports_per_vm                      = 65536


  icmp_idle_timeout_sec            = 30
  tcp_established_idle_timeout_sec = 1200
  tcp_transitory_idle_timeout_sec  = 30
  udp_idle_timeout_sec             = 30

  log_config {
    enable = true
    filter = "ALL"
  }
}
*/
