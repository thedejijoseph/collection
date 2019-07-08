# from ynonperek.com: python exercises

# write a program that takes a file name as command line argument,
# count how many times each word appears in the file and prints
# the word that appears the most (and its relevant count)

import os
import sys
# sys.argv is used to get the filename

from collections import Counter

try:
    script, filename = sys.argv
except:
	print("couldn't parse arguments")
	print("usage: python counter.py <filename>")
	sys.exit()

try:
	file = open(os.path.abspath(filename), 'r')
except:
	print(f"couldn't open file {filename} at {os.path.abspath(filename)}")

file = file.read().split()
count = Counter(file)

pick = count.most_common(1)[0]
print(f"most common: '{pick[0]}' appears {pick[1]} time(s)")
