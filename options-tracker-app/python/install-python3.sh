yum update -y
yum install https://repo.ius.io/ius-release-el$(rpm -E '%{rhel}').rpm
yum update -y
yum install -y python3
python3 --version
yum -y install coreutils
