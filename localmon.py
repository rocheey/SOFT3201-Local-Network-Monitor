#!/usr/bin/env python3
"""
local network monitoring application
soft3201
"""

import socket
import pexpect
import json


def get_hostname():
    result = socket.gethostname()
    return result


def run_command(command):
    child = pexpect.spawn(command)
    child.expect([pexpect.EOF, pexpect.TIMEOUT])
    command_output = child.before.decode()
    return command_output


print("Hostname:", get_hostname())


# Get network interface information
command = "ip -json link show"
command_output = run_command(command)

interfaces = json.loads(command_output)

print("Network interface information:")

for interface in interfaces:
    print("Interface name:", interface["ifname"])
    print("MTU:", interface["mtu"])
    print("MAC address:", interface.get("address", "Not available"))
    print("State:", interface.get("operstate", "Not available"))
    print("Flags:", interface.get("flags", []))
    print()


# Get IP address information
command = "ip -json address show"
command_output = run_command(command)

addresses = json.loads(command_output)

print("IP address information:")

for interface in addresses:
    print("Interface name:", interface["ifname"])

    for address in interface["addr_info"]:
        print("IP address:", address["local"])

    print()


# Get routing information
command = "ip -json route show"
command_output = run_command(command)

print("Routing information:")
print(command_output)
