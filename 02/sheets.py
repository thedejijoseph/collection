pizza = [
	[T,T,T,T,T],
	[T,M,M,M,T],
	[T,T,T,T,T],
]

def slice(pizza, r1, r2, c1, c2):
	P = pizza
	C1 = r1, c1
	C2 = r1, c2
	C3 = r2, c1
	C4 = r2, c2
	
	P[r1][c1]