#! /usr/bin/python3

import sys

previous_store = None
max_cost = 0

for line in sys.stdin:
	data = line.strip().split("\t")
	store, cost = data

	if previous_store and previous_store != store:
		print(f"{previous_store}\t{max_cost}")
		max_cost = 0

	cost = float(cost)
	if cost > max_cost:
		max_cost = cost

	previous_store = store

if previous_store:
	print(f"{store}\t{max_cost}")
