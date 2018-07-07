import random
import copy
import pprint

file = open("words.txt").read()
menu = set(file.splitlines())

# todo:
	# provide an interactive user interface
	# such that really specific requests can be made
	# like:
		# scramble  T R C H E A E 
		# the answer is 5 lettered and it starts 
		# with H
	
	# scramble loops with repeats
	# sort dish by length

def factorial(n):
	if n <= 1:
		return 1
	return n * factorial(n-1)

def scramble(k, l=0):
	# random scrambling using random.sample
	# provide l as desired length of scrambled output
	# default is the length of the input word
	
	width = len(k)
	entries = []
	
	if l is not 0 and l <= width:
		turns = factorial(width) / factorial(width - l)
		pass
	else:
		turns = factorial(width)
		l = width
	
	while len(entries) < turns:
		x = random.sample(k, l)
		if x not in entries:
			entries.append(x)
	
	return entries

def cook(order):
	print("parsing order")
	order = list(order.lower())
	
	min, max = 3, len(order)
	
	tray = []
	
	# secret sauce
	for l in range(min, max + 1):
		print(f"fetching {l} lettered words")
		fetch = scramble(order, l)
		for entry in fetch:
			entry = ''.join(entry)
			if entry in menu:
				tray.append(entry)
	
	tray.sort()
	
	return tray

order = input("what's your order: ")
dish = cook(order)
pprint.pprint(dish)