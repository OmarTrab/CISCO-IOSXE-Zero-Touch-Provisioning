# CISCO-IOSXE-Zero-Touch-Provisioning
ZTP(Zero-Touch Provisioning) automates the process of installing or upgrading software images,
and installing configuration files on Cisco catalyst switches that are deployed first time in the network.
It reduces manual tasks such as upgrading and configuring the devices.
When a device that supports Zero-Touch Provisioning boots up, and does not find the startup configuration
(during fresh install on Day Zero), the device enters the Zero-Touch Provisioning mode.
The device locates a Dynamic Host Configuration Protocol (DHCP) server, bootstraps itself with its interface IP address, gateway, and Domain Name System (DNS) server IP address, and enables Guestshell. 
The device then obtains the IP address or URL of a TFTP or HTTP server, and downloads a Python script to configure the device. 
Guestshell provides the environment for the Python script to run. Using this model, you can roll out hundreds of switches with fully customizable and without any error prone manual configuration process.

Incase if DHCP server is configured for PnP process, after receiving DHCP response the PnP agent process that is running on a Cisco IOS-XE device is initiated.
In the absence of the startup configuration it attempts to connect the PnP server and the PnP process is continued. In case Zero-Touch Provisioning and PnP fails,
the device falls back to auto install to load configuration files.

1)ZTP with HTTP server running on Ubuntu VM
In the dhcp.conf we have a sample sample DHCP server configuration with HTTPserver details. 
This server is connected either to the management port or front panel port of a switch. 
This DHCP server is running on a Linux Ubuntu VM.

2)Enable IOX,GUESTSHELL,VNIC FOR GUESTSHELL
In the guest-shell file we have a example that show us how to enable iox,vnic,guestshell on a Cisco Iosxe

3)Sample Ztp script.py configuration
In the ztp.py file configuration we have a simple script at wich configures the follow parameters:
  Interface,gateway,aaa,netconf-yang
  


