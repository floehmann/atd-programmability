#!/usr/bin/env python

# See getting started: 
# https://github.com/aristanetworks/cvprac#example
# sudo pip install cvprac

import sys
import pprint

# should just fix this
import urllib3
urllib3.disable_warnings()

from cvprac.cvp_client import CvpClient
clnt = CvpClient()

if len (sys.argv) != 2 :
    print "Usage: python sys.argv[0] ip_of_cvp"
    sys.exit (1)
else:
    cvphost = sys.argv[1]

clnt.connect([cvphost], 'arista', 'arista')
device_info = clnt.api.get_device_by_name('leaf1.arista.test')

pprint.pprint(device_info)
