#! /usr/bin/python3

import sys

hits_total = 0
previous_site = None

for line in sys.stdin:
	data = line.split("\t")
	site = data[0]

	if previous_site and previous_site != site:
		print(f"{previous_site}\t{hits_total}")
		hits_total = 0

	hits_total += 1
	previous_site = site

if previous_site:
	print(f"{previous_site}\t{hits_total}")