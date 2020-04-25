#! /usr/bin/python3

import sys

for line in sys.stdin:
	data = line.strip().split()
	if len(data) == 10:
		ip_address = data[0]
		print(f"{ip_address}\t1")