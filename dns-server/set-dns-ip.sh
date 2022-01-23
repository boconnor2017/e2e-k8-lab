#Run on photon
ifconfig eth0 172.16.0.9 netmask 255.255.255.0
route add default gateway 172.16.0.1
#Copy resolv.conf
