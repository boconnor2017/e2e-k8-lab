Kubernetes Home Lab

Step 1: Deploy Photon (photon-ova-4.0-ca7c9e9330.ova)

Step 2: Prep Photon Script
yum update
yum -y install git
cd /usr/local
git clone https://github.com/boconnor2017/e2e-k8-lab.git

Step 3: sh e2e-k8-minikube-start.sh

(Optional) Refresh script: refresh-e2e-k8-lab.sh
rm -rf /usr/local/e2e-k8-lab
git clone https://github.com/boconnor2017/e2e-k8-lab
