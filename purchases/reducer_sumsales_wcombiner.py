#! /usr/bin/python3

import sys

previous_day = None
n_days = 0
sales_sum = 0

for line in sys.stdin:
	data = line.strip().split("\t")
	day, price = data

	if previous_day and previous_day != day:
		print(f"{previous_day}\t{sales_sum}")
		n_days, sales_sum = 0, 0

	n_days += 1
	sales_sum += float(price)
	previous_day = day

if previous_day:
	print(f"{previous_day}\t{sales_sum}")