#!/usr/bin/env python
#Prerequisite: DNS Server and entries need to be completed

import pyVim
from pyVim import connect

host_ip = "" #Enter IP Address of ESXi Host
host_pass = "" #Enter Password of ESXi Host

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
