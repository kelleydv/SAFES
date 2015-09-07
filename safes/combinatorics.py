"""
Implements basic combinatorial functions.
Also available in the Standard Library.
"""

def factorial(n):
	if n < 0:
		raise ValueError('factorial(%d): n! is not defined for n < 0.' % n)
	elif n == 0:
		return 1
	else:
		return n*factorial(n-1)

def permute(n,r):
	return factorial(n)/factorial(n-r)

def choose(n,r):
	return factorial(n)/(factorial(r)*factorial(n-r))
