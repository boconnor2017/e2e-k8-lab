yum -y install unbound
cp /etc/unbound/unbound.conf /etc/unbound/unbound.conf_BACKUP
rm -f /etc/unbound/unbound.conf
curl https://raw.githubusercontent.com/boconnor2017/e2e-k8-lab/main/dns-server/unbound.conf >> /etc/unbound/unbound.conf
