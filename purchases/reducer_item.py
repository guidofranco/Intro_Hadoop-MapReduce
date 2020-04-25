#! /usr/bin/python3

import sys

sales_total = 0
previous_item = None

for line in sys.stdin:
    data = line.strip().split("\t")
    actual_item, cost = data

    if previous_item and previous_item != actual_item:
        print(f"{previous_item}\t{sales_total}")
        sales_total = 0
    
    previous_item = actual_item
    sales_total += float(cost)

if previous_item != None:
    print(f"{previous_item}\t{sales_total}")