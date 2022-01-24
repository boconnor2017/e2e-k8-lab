yum -y install unbound
cp /etc/unbound/unbound.conf /etc/unbound/unbound.conf_BACKUP
rm -f /etc/unbound/unbound.conf
