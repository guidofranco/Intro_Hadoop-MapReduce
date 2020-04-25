#! /usr/bin/python3

import sys

previous_site = None
total_hits = 0
most_visited_site = None
max_hits = 0

for line in sys.stdin:
	site, hit = line.split("\t")

	if previous_site and previous_site != site:
		if total_hits > max_hits:
			max_hits = total_hits
			most_visited_site = previous_site

		total_hits = 0

	total_hits += 1
	previous_site = site

if previous_site:
	if total_hits > max_hits:
		max_hits = total_hits
		most_visited_site = previous_site

print(f"{most_visited_site}\t{max_hits}")