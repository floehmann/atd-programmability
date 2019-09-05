#!/usr/bin/env python

import sys
import pyeapi
import pprint
import argparse

parser = argparse.ArgumentParser(description='Show Arista switch user details')
parser.add_argument('host', type=str, help='switch management interface')
parser.add_argument('port', type=str, help='switch management port')
parser.add_argument('admin', type=str, help='switch admin user login')
parser.add_argument('password', type=str, help='switch admin password')
parser.add_argument('user', type=str, help='switch user to check')

args = parser.parse_args()

node = pyeapi.connect(host=args.host, port=args.port, username=args.admin, password=args.password, return_node=True)

users = node.api('users')

response = users.get(args.user)

pprint.pprint(response)

