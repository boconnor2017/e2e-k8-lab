Kubernetes Home Lab

Step 1: Deploy Photon (photon-ova-4.0-ca7c9e9330.ova)
Step 1a: default password is changeme
Step 1b: recommended working directory is /usr/local

Step 2: Prep Photon Script 'vi prep-photon.sh'
curl https://raw.githubusercontent.com/boconnor2017/e2e-k8-lab/main/prep-photon.sh >> prep-photon.sh

Step 3 (optional):
curl https://raw.githubusercontent.com/boconnor2017/e2e-k8-lab/main/refresh-e2e-k8-lab.sh >> refresh-e2e-k8-lab.sh

Step 4: sh prep-photon-sh
Step 5 (optional): sh refresh-e2e-k8-lab.sh

Step 6: (from e2e-k8-lab dir) sh e2e-k8-minikube-start.sh


**********************************************************
*******  LABS ********************************************
**********************************************************

Lab 01: Options Tracker App 
Step 1: cd /usr/local/e2e-k8-lab/options-tracker-app
Step 2: sh build-app.sh

Lab 02: Prerequisites for Tanzu
Step 1: cd /usr/local/e2e-k8-lab/dns-server
Step 2: sh set-dns-ip.sh 
Step 3: sh build-dns-server.sh
