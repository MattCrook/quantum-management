resource "google_cloudbuildv2_repository" "quantum_management" {
  name              = "quantum-management"
  parent_connection = google_cloudbuildv2_connection.svc_github_connection.name
  remote_uri        = "https://github.com/MattCrook/quantum-management.git"
}

resource "google_cloudbuild_trigger" "quantum_management_push_to_main" {
  name     = "push-to-main-quantum-management"
  location = "us-central1"
  project  = var.project_id

  repository_event_config {
    repository = resource.google_cloudbuildv2_repository.quantum_management.id
    push {
      branch = "master"
    }
  }
  filename = ".deployment/no_tag_name_cloudbuild.yaml"

  service_account = "567594519343-compute@developer.gserviceaccount.com"
}


resource "google_cloudbuildv2_connection" "svc_github_connection" {
  location = "us-central1"
  name     = "svc-github-connection"
  project  = var.project_id

  github_config {
    app_installation_id = 24919336

    authorizer_credential {
      # https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/secret_manager_secret.html
      oauth_token_secret_version = ""
    }
  }
}


###################
resource "google_cloudbuildv2_repository" "quantum_management_stg" {
  name              = "quantum-management-stg"
  parent_connection = google_cloudbuildv2_connection.svc_github_connection.id
  remote_uri        = "https://github.com/MattCrook/quantum-management.git"
}

resource "google_cloudbuild_trigger" "quantum_management_stg" {
  name     = "quantum-management-stg"
  location = "us-central1"
  project  = var.project_id

  repository_event_config {
    repository = resource.quantum_management_stg.id
    push {
      branch = "development"
    }
  }
  filename = ".deployment/cloudbuild.yaml"
  service_account = "567594519343-compute@developer.gserviceaccount.com"
}

resource "google_clouddeploy_delivery_pipeline" "quantum_management_stg" {
  name        = "quantum-management-pipeline-stg"
  location    = "us-central1"
  project     = var.project_id
  description = ""
  serial_pipeline {
    stages {
      target_id = ""
    }
  }
}

resource "google_clouddeploy_delivery_pipeline_iam_binding" "quantum_management_deploy_binding" {
  for_each = {
    for pipeline in [
      google_clouddeploy_delivery_pipeline.quantum_management_stg,
    ] :
    pipeline.name => pipeline
  }
  project  = var.project_id
  location = each.value.location
  name     = each.value.name
  role     = "roles/clouddeploy.releaser"
  members = [
    "serviceAccount:567594519343-compute@developer.gserviceaccount.com"
  ]
}
