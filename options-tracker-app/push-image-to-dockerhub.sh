# PREREQ: Login to dockerhub using docker login -u vmwe2e -p <password>
docker tag options-tracker-app-001  vmwe2e/options-tracker-app-001
docker push vmwe2e/options-tracker-app-001 