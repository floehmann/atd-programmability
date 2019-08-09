#!/usr/bin/python

import sys
import pyeapi
import pprint

if len(sys.argv) < 2:
    user = 'testuser'
else:
    user = str(sys.argv[1])

print user
 
node = pyeapi.connect(host='192.168.0.14',username='arista',password='arista',return_node=True)

users = node.api('users')

response = users.get(user)

pprint.pprint(response)

