#! /usr/bin/python3

import sys

for line in sys.stdin:
	data = line.split('"')
	if len(data) == 3:
		request = data[1].split()
		if len(request) == 3:
			method, site, protocol = request
			print(f"{site}\t1")