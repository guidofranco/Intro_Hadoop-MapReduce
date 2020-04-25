#! /usr/bin/python3

import sys

sales_total = 0
n_sales = 0

for line in sys.stdin:
	cost = float(line.strip())
	sales_total += cost
	n_sales += 1

print(f"Total values of sales: {round(sales_total, 2)}")
print(f"Number of sales: {n_sales}")