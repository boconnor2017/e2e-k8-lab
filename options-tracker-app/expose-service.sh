# MINIKUBE ONLY: open second SSH session, and run minikube tunnel
kubectl expose deployment options-tracker-app --type=LoadBalancer --port=80
