import cli
from cli import configurep
from cli import executep

print "\n\n *** ZTP Script *** \n\n"
cli.configurep(["hostname ROUTERZTP"])
print "Configure vlan interface, gateway, aaa, and enable netconf-yang\n\n"
cli.configurep(["int GigabitEthernet0", "ip address 192.168.1.60 255.255.255.0", "no shut", "end"])
cli.configurep(["username admin privilege 15 secret 0 Test123"])
cli.configurep(["aaa new-model", "aaa authentication login default local", "end"])
cli.configurep(["aaa authorization exec default local", "aaa session-id common", "end"])
cli.configurep(["netconf-yang", "end"])
cli.configurep(["ip http secure-server", "restconf", "end"])
cli.configurep(["line vty 0 15", "transport input all", "exec-timeout 0 0", "end"])
print "\n\n *** Executing show ip interface brief  *** \n\n"
cli_command = "show ip int brief"
cli.executep(cli_command)
print "\n\n *** ZTP Script Execution Complete *** \n\n"
