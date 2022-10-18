#!/usr/bin/env python3


from scapy.all import *
import sys
sr(IP(dst=sys.argv[1])/ICMP())