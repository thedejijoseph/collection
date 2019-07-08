# 02072018; 1433
# reading and re-learning algebra => artificial intelligence

# matrix multiplication
def matmul(A, B):
	"""Perform a matrix multiplication of two matrices."""
	
	# matrix A should have the same columns as B as rows.
	if len(A) != len(B):
		raise ParseError("Incompatible matrices of differing sizes.")
		return
		
	# where A is a multidimension array and B is singled
	# result is a matrix size of B
	result = []
	for x in B:
		r = 0
		for y in A[B.index(x)]:
			r += x*y
		result.append(r)
	
	return result

A = [
  [0,2],
  [1,2]]
 
B = [2,3]
print(matmul(A, B))