#! /usr/bin/python3

import sys
import csv

from datetime import datetime

week_dict = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}

csv_reader = csv.reader(sys.stdin, delimiter="\t")

for line in csv_reader:
	if len(line) == 6:
		date, price = line[0].strip(), line[4].strip()
		n_weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
		weekday = week_dict[n_weekday]
		print(f"{weekday}\t{price}")
		
