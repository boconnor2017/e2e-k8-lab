#Run on photon
echo Changing IP Address..
echo You are about to lose your SSH Session!
echo Start a new session at 172.16.0.9
echo
ifconfig eth0 172.16.0.9 netmask 255.255.255.0
route add default gateway 172.16.0.1
