# from ynonperek.com: python exercises

# write a program that asks the user for a number (integer only)
# and prints the sum of its digits

import logging

try:
	digit = input("number (integer only): ")
	int(digit)
except ValueError as e:
	# print("enter an integer only!")
	#logging.error(e)
	pass

digits = [int(d) for d in digit]
print(f"the sum of {digit} is {sum(digits)}")