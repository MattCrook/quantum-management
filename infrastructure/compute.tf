# https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_template
# https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_from_template

data "google_compute_subnetwork" "usc1_default_subnet" {
  project = var.project_id
  name    = "default"
  region  = "us-central1"
}

resource "google_service_account" "quantum_management" {
  project      = var.project_id
  account_id   = "quantum-management-sa"
  display_name = "quantum-management-compute-sa"
}

resource "google_compute_instance_template" "quantum_management" {
  provider       = google-beta
  project        = var.project_id
  region         = var.region
  name           = "quantum-management-instance-tpl"
  machine_type   = "e2-medium"
  can_ip_forward = false
  tags = [
    "quantum-management",
  ]

  metadata_startup_script = templatefile("./startup_script.sh", {
    TAG          = "2.0"
    EXPOSED_PORT = "80"
  })

  disk {
    source_image = "ubuntu-os-cloud/ubuntu-2004-lts"
    device_name  = "root-disk"
  }

  service_account {
    email  = google_service_account.quantum_management.email
    scopes = ["cloud-platform"]
  }

  network_interface {
    network    = "default"
    subnetwork = data.google_compute_subnetwork.usc1_default_subnet.id
  }

  scheduling {
    preemptible       = false
    automatic_restart = true
  }

  metadata = {
    enable-oslogin = "TRUE"
  }
}


resource "google_compute_instance_from_template" "quantum_management" {
  name                     = "quantum-management"
  zone                     = var.zone
  source_instance_template = google_compute_instance_template.quantum_management.self_link_unique
  labels = {
    app = "quantum-management"
  }
}
