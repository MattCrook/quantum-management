#-------Service Account-----------#
#--------------------------------#
resource "google_service_account" "quantum_management" {
  project      = var.project_id
  account_id   = "quantum-management-sa"
  display_name = "quantum-management-compute-sa"
}

# resource "google_project_iam_member" "quantum_management_sa_networkUser" {
#   project  = var.project_id
#   role     = "roles/compute.networkUser"
#   member   = "serviceAccount:${google_service_account.quantum_management.email}"
# }

# resource "google_project_iam_member" "quantum_management_sa_instanceAdmin_v1" {
#   project  = var.project_id
#   role     = "roles/compute.instanceAdmin.v1"
#   member   = "serviceAccount:${google_service_account.quantum_management.email}"
# }

#--------------- COMPUTE INSTANCE -----------#
#--------------------------------------------#
resource "google_compute_instance" "quantum_management" {
  name                = "quantum-management"
  project             = var.project_id
  zone                = var.zone
  machine_type        = "e2-medium"
  can_ip_forward      = false
  deletion_protection = false
  enable_display      = true
  labels              = { application = "quantum_management" }
  tags = [
    # These allow http and https traffic (check boxes in UI)
    "http-server",
    "https-server",
    "quantum-management",
    "allow-quantum-ssh",
  ]

  allow_stopping_for_update = true

  metadata = {
    google-logging-enabled    = "true"
    google-monitoring-enabled = "true"
    enable-oslogin            = "TRUE"
    ssh-keys                  = "root:${file("~/.ssh/quantum_rsa.pub")}"
    startup-script = templatefile("./scripts/startup_script.sh", {
      EXPOSED_PORT     = "80"
      REPO             = "mgcrook11/quantum-management-public"
      TAG              = "1.6"
      #ENVIRONMENT      = "development"
    })
  }

  boot_disk {
    auto_delete = true
    device_name = "quantum-management"

    initialize_params {
      image = "projects/cos-cloud/global/images/cos-105-17412-535-55"
      size  = 10
      type  = "pd-balanced"
    }
  }

  network_interface {
    network     = "default"
    subnetwork  = "projects/quantum-management-295116/regions/us-central1/subnetworks/default"
    stack_type  = "IPV4_ONLY"
    queue_count = 0

    access_config {
      network_tier = "PREMIUM"
    }
  }

  # service_account {
  #   email  = google_service_account.quantum_management.email
  #   scopes = ["cloud-platform"]
  # }

  service_account {
    email  = "567594519343-compute@developer.gserviceaccount.com"
    scopes = ["https://www.googleapis.com/auth/cloud-platform"]
    #scopes = [
    #  "https://www.googleapis.com/auth/devstorage.read_only",
    #  "https://www.googleapis.com/auth/logging.write",
    #  "https://www.googleapis.com/auth/monitoring.write",
    #  "https://www.googleapis.com/auth/service.management.readonly",
    #  "https://www.googleapis.com/auth/servicecontrol",
    #  "https://www.googleapis.com/auth/trace.append"
    #  ]
  }

  scheduling {
    automatic_restart   = true
    on_host_maintenance = "MIGRATE"
    preemptible         = false
    provisioning_model  = "STANDARD"
  }

  shielded_instance_config {
    enable_integrity_monitoring = true
    enable_secure_boot          = false
    enable_vtpm                 = true
  }
}
