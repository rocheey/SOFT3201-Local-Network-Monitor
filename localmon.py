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
	child.expect([pexpect.EOF, pexpext.TIMEOUT])
	command_output = child.before.decode()
	return command_output
	
print("Hostname:", get_hostname())

command = "ip -json link show"
command_output = run_command(command)

print("Network interface information:")
print(command_output)





