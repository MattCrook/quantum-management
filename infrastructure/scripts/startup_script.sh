#!/bin/bash

# prints each command and its arguments to the standard error (stderr) before executing it.
set +x

# sudo docker run -it -d --name quantummanagement -e ENVIRONMENT='development' -p 80:8000 mgcrook11/quantum-management-public:1.4


#--------------------#
# https://docs.docker.com/engine/reference/commandline/login/#credentials-store
# https://stackoverflow.com/questions/38520729/docker-login-with-root-user-on-container-vm-image
# https://cloud.google.com/container-optimized-os/docs#accessing_private_google_container_registry

sudo docker pull ${REPO}:${TAG}
sudo docker run -it -d --name quantummanagement -p ${EXPOSED_PORT}:8000 ${REPO}:${TAG}

#-----------------------#

sudo apt -y update
sudo apt install -y net-tools
apt install -y jq

sudo apt -y update
sudo apt -y install curl
sudo apt -y install ping


SDA=$(sudo blkid /dev/sda)
FSTAB1=$(cat /etc/fstab)
HOSTNAME=$(curl -H "Metadata-Flavor: Google" "http://metadata.google.internal/computeMetadata/v1/instance/hostname")
ID=$(curl -H "Metadata-Flavor: Google" "http://metadata.google.internal/computeMetadata/v1/instance/id")
INSTANCE_INTERNAL_IP=$(curl -H "Metadata-Flavor: Google" "http://metadata.google.internal/computeMetadata/v1/instance/network-interfaces/0/ip")
METADATA=$(curl -f -H "Metadata-Flavor: Google" "http://metadata.google.internal/computeMetadata/v1/instance/attributes/?recursive=True" | jq 'del(.["startup-script"])')
DOCKER=$(docker system info)
ALL_METADATA=$(curl -H "Metadata-Flavor: Google" "http://compute.googleapis.com/compute/v1/projects/quantum-management-295116/zones/us-central1-a/instances/quantum-management")

mkdir /tmp/health-test
touch /tmp/health-test/index.html
chmod 777 /tmp/health-test/index.html


cat >/tmp/health-test/index.html <<EOF
    <h2>Quantum Management Test Internal Webpage</h2>
    <h3>I am Healthy</h3>
    <div style="margin-top: 1rem:"></div>
    <h4>HostName: $${HOSTNAME}</h4>
    <pre>
        Metadata: $${METADATA}
        SDA: $${SDA}
        /etc/fstab: $${FSTAB1}
        IP: $${INSTANCE_INTERNAL_IP}
        ID: $${ID}
    </pre>
    <div>
        DOCKER:
    </div>
    <pre>
      $${DOCKER}
    </pre>
    <div>
    ALL METADATA:
    </div>
    <pre>
    $${ALL_METADATA}
    </pre>
EOF

sudo docker run -d -p 8080:80 --name healthtest -v /tmp/health-test/:/usr/share/nginx/html:ro nginx
