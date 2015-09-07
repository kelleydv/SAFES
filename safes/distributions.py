from .combinatorics import choose


class Binomial:
	"""
	Models the binomial distribution:
	The probability of observing X
	successes in n trials.
	"""
	
	def __init__(self, n=0, p=1):
		if not 0 <= p <= 1:
			raise ValueError('Binomial() instance with p=%s' % str(p))
		self.n = n
		self.p = p
		self.q = 1-p

	def P(self, X=0):
		"""
		Return the probability of observing X successes
		"""
		if X < 0 or not isinstance(X, int):
			raise ValueError('Binomial.p(%s): this input is not in the domain' % str(X))
		if X > self.n:
			return 0
		return choose(self.n, X)*(self.p**X)*self.q**(self.n-X)

	def P_left(self, X=0):
		"""
		Return the probability of observing at most X successes
		"""
		a = 0
		while X >=0:
			a += self.P(X)
			X -= 1
		return a

	def P_right(self, X=0, precision=10**-6):
		"""
		Return the probability of observing at least X successes
		"""
		a = 0
		p = precision + 1
		while p > precision:
			p = self.P(X)
			a += p
			X += 1
		return a
