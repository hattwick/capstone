#ip addr test
# __author__ = 'phil'

import random
import sys

def subnet_calc():
    try:
        print "\n"

        # Check for valid IP
        while True:
            ip_address = raw_input("Enter IP Address: ")
            a = ip_address.split('.')
            print aif (len(a) = 4) and (1 <= int(a[0] <= 223 ) and (int(a[0]) != 127)
