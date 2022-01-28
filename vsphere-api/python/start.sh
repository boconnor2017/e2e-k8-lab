curl https://raw.githubusercontent.com/boconnor2017/e2e-k8-lab/main/options-tracker-app/python/install-python3.sh >> install-python3.sh
sh install-python3.sh
yum -y install git
python3 -m pip install pyvmomi
python3 -m pip install git+https://github.com/vmware/pyvmomi.git
python3 build-tanzu-lab.py
