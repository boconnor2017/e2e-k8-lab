#!/usr/bin/env python
#Prerequisite: DNS Server and entries need to be completed

import pyVim
from pyVim import connect

host_ip = "172.16.0.201"
host_pass = "VMware1!"

#Connect to a host
my_cluster = connect.ConnectNoSSL(host_ip, 443, "root", host_pass)
print("Connected to host "+host_ip)

#parser = cli.Parser()
#args = parser.get_args()
#si = service_instance.connect(my_cluster)

content = my_cluster.RetrieveContent()
for child in content.rootFolder.childEntity:
    if hasattr(child, 'vmFolder'):
        datacenter = child
        vmfolder = datacenter.vmFolder
        vmlist = vmfolder.childEntity
        for vm in vmlist:
            print(vm)

connect.Disconnect(my_cluster)
