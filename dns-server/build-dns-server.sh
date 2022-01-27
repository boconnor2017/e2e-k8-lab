iptables -A INPUT -i eth0 -p udp --dport 53 -j ACCEPT
iptables-save >/etc/systemd/scripts/ip4save
iptables -L
systemctl disable systemd-resolved.service
systemctl stop systemd-resolved
rm -f /etc/resolv.conf
cp resolv.conf /etc/resolv.conf
curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
docker-compose --version
docker-compose up
