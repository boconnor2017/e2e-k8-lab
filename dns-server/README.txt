DNS server on PhotonOS

Troubleshooting: if port 53 binding fails due to (similar error as): error: can't bind socket: Address already in use for 0.0.0.0 port 53
Step 1: systemctl disable systemd-resolved.service
Step 2: systemctl stop systemd-resolved
Step 3: vi /etc/resolv.conf
Step 4: add 8.8.8.8 to namespace
