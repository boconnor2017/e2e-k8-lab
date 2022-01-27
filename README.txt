Kubernetes Home Lab

Step 1: Deploy Photon (photon-ova-4.0-ca7c9e9330.ova)
Step 1a: default password is changeme
Step 1b: recommended working directory is /usr/local

Step 2: Prep Photon Script 'vi prep-photon.sh'
curl https://raw.githubusercontent.com/boconnor2017/e2e-k8-lab/main/prep-photon.sh >> prep-photon.sh

Step 3 (optional):
curl https://raw.githubusercontent.com/boconnor2017/e2e-k8-lab/main/refresh-e2e-k8-lab.sh >> refresh-e2e-k8-lab.sh

Step 4: sh prep-photon.sh
Step 5 (optional): sh refresh-e2e-k8-lab.sh


**********************************************************
*******  LABS ********************************************
**********************************************************

Lab 01: Minkube (all labs with *01 requre minikube to be running)
Step 1: cd /usr/local/e2e-k8-lab/
Step 2: sh e2e-k8-minikube-start.sh

Lab 02: Options Tracker App (*01)
Step 1: cd /usr/local/e2e-k8-lab/options-tracker-app
Step 2: sh build-app.sh

Lab 03: Build local DNS server for lab
Step 1: cd /usr/local/e2e-k8-lab/dns-server
Step 2: sh set-dns-ip.sh #Note: there are network specific configurations that you may need to edit before running this, default subnet 172.16.0.0/24
Step 3: sh build-dns-server.sh
Step 4: login to UI at http://<DNS Server IP Address>:5380
