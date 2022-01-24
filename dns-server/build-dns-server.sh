#yum -y install unbound
#cp /etc/unbound/unbound.conf /etc/unbound/unbound.conf_BACKUP
#rm -f /etc/unbound/unbound.conf
#curl https://raw.githubusercontent.com/boconnor2017/e2e-k8-lab/main/dns-server/unbound.conf >> /etc/unbound/unbound.conf
#cat /etc/unbound/unbound.conf
iptables -A INPUT -i eth0 -p udp --dport 53 -j ACCEPT
iptables-save >/etc/systemd/scripts/ip4save
iptables -L
systemctl disable systemd-resolved.service
systemctl stop systemd-resolved
#systemctl enable unbound
#systemctl start unbound
#systemctl status unbound
#unbound -V
rm -f /etc/resolv.conf
cp resolv.conf /etc.resolv.conf
docker run --name my-unbound -d -p 53:53/udp -p 53:53/tcp \
--restart=always mvance/unbound:latest
