iptables -A INPUT -i eth0 -p udp --dport 53 -j ACCEPT
iptables-save >/etc/systemd/scripts/ip4save
iptables -L
systemctl disable systemd-resolved.service
systemctl stop systemd-resolved
rm -f /etc/resolv.conf
cp resolv.conf /etc/resolv.conf
docker build -t e2e-local-dns-01 .
