#! /usr/bin/python3

import sys

def calculate_std(a_list):
	mean = sum(a_list) / len(a_list)
	deviations_sum = list(map(lambda x: (x - mean) ** 2, a_list))
	deviations_sum = sum(deviations_sum)
	std = (deviations_sum / len(a_list)) ** (0.5)
	return std

previous_day = None
sales_list = []

for line in sys.stdin:
	data = line.split("\t")
	day, price = data

	if previous_day and day != previous_day:
		sales_list = list(map(lambda x: float(x), sales_list))
		mean = sum(sales_list) / len(sales_list)
		mean = round(mean, 2)
		print(f"{previous_day}\t{mean}")
		sales_list = []

	sales_list.append(price)
	previous_day = day

if previous_day:
	sales_list = list(map(lambda x: float(x), sales_list))
	mean = sum(sales_list) / len(sales_list)
	mean = round(mean, 2)
	print(f"{previous_day}\t{mean}")