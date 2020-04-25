#! /usr/bin/python3

import sys

#URLS = ["http://www.the-associates.co.uk", "http://the-associates.co.uk"]
URL = "http://www.the-associates.co.uk"

for line in sys.stdin:
	data = line.strip().split('"')
	data = data[1].split()
	if len(data) == 3:
		method, site, protocol = data
		if site.startswith(URL):
			site = site.replace(URL, "")
		print(f"{site}\t1")
