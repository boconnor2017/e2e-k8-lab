# MINIKUBE ONLY
kubectl expose deployment options-tracker-app --type=LoadBalancer --port=80
minikube service options-tracker-app
