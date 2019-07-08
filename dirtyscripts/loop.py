# how far/deep can recursions go

def mul(n, i=0):
	print(i)
	if i == 0:
		try:
			return n * mul(n*n)
		except:
			return n
	for k in range(i):
		return n * mul(n*n)

print(mul(6, 2))