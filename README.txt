Kubernetes Home Lab

Step 1: Deploy Photon (photon-ova-4.0-ca7c9e9330.ova)
Step 1a: default password is changeme
Step 1b: recommended working directory is /usr/local

Step 2: Prep Photon Script 'vi prep-photon.sh'
wget https://raw.githubusercontent.com/boconnor2017/e2e-k8-lab/main/prep-photon.sh >> prep-photon.sh

Step 3: sh prep-photon-sh
Step 4: (from e2e-k8-lab dir) sh e2e-k8-minikube-start.sh

(Optional) Refresh script: refresh-e2e-k8-lab.sh
rm -rf /usr/local/e2e-k8-lab
git clone https://github.com/boconnor2017/e2e-k8-lab


**********************************************************
*******  LABS ********************************************
**********************************************************

Lab 01: Options Tracker App 
Step 1: cd /usr/local/e2e-k8-lab/options-tracker-app
Step 2: sh build-app.sh
