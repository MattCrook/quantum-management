#!/bin/bash

# prints each command and its arguments to the standard error (stderr) before executing it.
set +x

# tells the shell to exit the script if any command returns a non-zero exit status (an indication of failure in Unix-like systems)
# set -e

# disable the debugging output just before the sensitive command and re-enable it afterward
# set -x

# uninstall all old packages
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done


#########################################################
# sudo apt-get update
# sudo apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release
# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
# echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
# sudo apt-get update
# sudo apt-get install docker -y
# sudo apt update
# sudo apt install -y --force-yes docker-ce
# USERNAME=$(cat /tmp/docker.username)
# cat /tmp/docker.password | sudo docker login -u $USERNAME --password-stdin

# sudo docker pull mgcrook11/quantum-management:$TAG
# sudo docker run -it -d --name quantummanagement -p $EXPOSED_PORT:8000 mgcrook11/quantummanagement:$TAG

#########################################################

# Check docker systemctl status
DOCKER_STATUS=$(systemctl is-active docker.service)

if [[ $$DOCKER_STATUS == 'active' ]]; then
	systemctl stop docker.service
fi

# Setup docker data dir used for transient storage
if [ -d /var/lib/docker ]; then
	rm -fr /var/lib/docker
fi

# Setup docker run dir for pid files
sudo mkdir -p /var/lib/docker/
sudo chown -R root:adm /lib/run/docker


pushd /tmp || exit
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt -y update
sudo apt install -y docker-ce docker-ce-cli containerd.io
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
popd || return

#sudo touch /usr/local/bin/exec-pre-start
#sudo chmod 755 /usr/local/bin/exec-pre-start

sudo cat > /usr/local/bin/exec-pre-start <<EOF
#!/bin/bash
set -e
set -o pipefail
# Check to make sure PID directory exists
if [ ! -d "/var/run/docker.pid" ]; then
  sudo mkdir -p /var/run/docker.pid/
  sudo chown -R root:adm /var/run/docker.pid
fi

# Enable ipv4 forwarding, required on CIS hardened machines
sudo echo "net.ipv4.conf.all.forwarding=1" > /etc/sysctl.d/enabled_ipv4_forwarding.conf
EOF

sudo chmod 755 /usr/local/bin/exec-pre-start


# Install and start docker systemd unit
cat >/etc/systemd/system/docker.service <<EOF
[Unit]
Description=Docker Service
After=network.target
[Service]
User=root
Group=adm
Type=simple
Restart=always
RestartSec=5
ExecStartPre=/usr/local/bin/exec-pre-start
ExecStart=
ExecReload=/bin/kill -HUP \$$MAINPID
PIDFile=/var/run/docker.pid
LimitNOFILE=65536
[Install]
WantedBy=multi-user.target
EOF

sudo systemctl enable docker
sudo systemctl start docker

sudo docker pull mgcrook11/quantum-management:$TAG
sudo docker run -it -d --name quantummanagement -p $EXPOSED_PORT:8000 mgcrook11/quantummanagement:$TAG


########################################
# Install couple more tools, and create a basic HTML page we will use to healthcheck
#############################################

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
