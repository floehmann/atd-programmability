#!/usr/bin/env python

import sys
import pyeapi
import pprint

if len(sys.argv) < 2:
    user = 'testuser'
else:
    user = str(sys.argv[1])

print user
 
node = pyeapi.connect(host='192.168.0.14',username='arista',password='arista',return_node=True)

# run it locally
# ssh -L 8080:192.168.0.14:443 arista@external-atd-ip
# https://127.0.0.1:8080/explorer.html
#node = pyeapi.connect(host='127.0.0.1',port='8080',username='arista',password='arista',return_node=True)

users = node.api('users')

response = users.get(user)

pprint.pprint(response)

