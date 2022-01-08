# PREREQ: Login to dockerhub using docker login -u vmwe2e -p <password>
docker tag boc-base-python-image-001 vmwe2e/boc-base-python-image-001
docker push vmwe2e/boc-base-python-image-001
