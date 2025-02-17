#!/bin/bash

# prints each command and its arguments to the standard error (stderr) before executing it.
set +x

# uninstall all old packages
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done

# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "bookworm") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin


sudo docker pull mgcrook11/quantum-management:$TAG
sudo docker run -it -d --name quantummanagement -p $EXPOSED_PORT:8000 mgcrook11/quantummanagement:$TAG

#-------------------------------------------------------#

sudo apt -y update
sudo apt install -y net-tools
apt install -y jq

sudo apt -y update
sudo apt -y install curl
sudo apt -y install ping
# sudo apt install -y netstat

SDA=$(sudo blkid /dev/sda)
FSTAB1=$(cat /etc/fstab)
NAME=$(curl -H "Metadata-Flavor: Google" "http://metadata.google.internal/computeMetadata/v1/instance/hostname")
METADATA=$(curl -f -H "Metadata-Flavor: Google" "http://metadata.google.internal/computeMetadata/v1/instance/attributes/?recursive=True" | jq 'del(.["startup-script"])')
DOCKER=$(docker system info)

mkdir /tmp/health-test
touch /tmp/health-test/index.html
chmod 777 /tmp/health-test/index.html


cat >/tmp/health-test/index.html <<EOF
    <h2>Quantum Management Test Internal Webpage</h2>
    <h3>$${NAME}</h3>
    <h4>I am Healthy</h4>
    <pre>
        Metadata: $${METADATA}
        SDA: $${SDA}
        /etc/fstab: $${FSTAB1}
        IP: $${IP}
        ID: $${ID}
    </pre>
    <div>
        DOCKER:
    </div>
    <pre>
      $${DOCKER}
    </pre>
EOF

sudo docker run -d -p 8080:8080 --name healthtest -v /tmp/health-test/:/usr/share/nginx/html:ro nginx
