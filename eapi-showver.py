#!/usr/bin/python

import pprint
from jsonrpclib import Server

# NOTE: Externalize config and secrets!
switch = Server ("http://arista:arista@192.168.0.14/command-api")

response = switch.runCmds( 1, ["show version"] )

print
print "The switch model name is " + response[0]["modelName"] + " and it is running " + response[0]["version"]
print "\nHere is the json response:\n"
print response
print "\nHere is the pretty json response:\n"
pprint.pprint(response)
print 

