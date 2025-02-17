#!/bin/bash

set +x

SDA=$(sudo blkid /dev/sda)
FSTAB1=$(cat /etc/fstab)
NAME=$(curl -H "Metadata-Flavor: Google" "http://metadata.google.internal/computeMetadata/v1/instance/hostname")
METADATA=$(curl -f -H "Metadata-Flavor: Google" "http://metadata.google.internal/computeMetadata/v1/instance/attributes/?recursive=True" | jq 'del(.["startup-script"])')
DOCKER=$(docker system info)
ALL_METADATA=$(https://metadata.google.internal/computeMetadata/v1/instance)

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
    <div>
    ALL METADATA:
    </div>
    <pre>
    $${ALL_METADATA}
    </pre>
EOF

sudo docker run -d -p 8080:80 --name healthtest -v /tmp/health-test/:/usr/share/nginx/html:ro nginx
