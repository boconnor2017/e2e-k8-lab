#!/usr/bin/env python
#Prerequisite: DNS Server and entries need to be completed
#Parameters: <ESXi Host IP Address> <ESXi Host Password>

import pyVim
from pyVim import connect
import sys

def err_log(err):
    print(err)
    return

def paramcheck(args):
    paramlen = len(args)
    if paramlen == 3:
        return 1
    else:
        return 0

def connect_esxi_host(args):
    host_ip = args[1]
    host_pass = args[2]
    e2e_host = connect.ConnectNoSSL(host_ip, 443, "root", host_pass)
    return e2e_host

def disonnect_esxi_host(e2e_host):
    connect.Disconnect(e2e_host)
    return

def get_vm_list(e2e_host):
    content = e2e_host.RetrieveContent()
    for child in content.rootFolder.childEntity:
        if hasattr(child, 'vmFolder'):
            datacenter = child
            vmfolder = datacenter.vmFolder
            vmlist = vmfolder.childEntity
            return vmlist

args = sys.argv
if paramcheck(args) == 1:
    err_log("Connecting to host: "+args[1])
    e2e_host = connect_esxi_host(args)
    err_log("Connected!")

    err_log("Getting VM List...")
    vmlist = get_vm_list(e2e_host)
    err_log("Returned a list of "+str(len(vmlist))+" vms.")

    disonnect_esxi_host(e2e_host)
else:
    err_log("ERROR: Please enter 2 parameters - Host IP and Password")

