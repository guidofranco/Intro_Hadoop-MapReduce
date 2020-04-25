#! /usr/bin/python3

import sys

previous_ip = None
total_hits = 0

for line in sys.stdin:
	actual_ip, hit = line.split()

	if previous_ip and previous_ip != actual_ip:
		print(f"{previous_ip}\t{total_hits}")
		total_hits = 0

	total_hits += 1
	previous_ip = actual_ip

if previous_ip:
	print(f"{previous_ip}\t{total_hits}")