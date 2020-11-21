from random import randrange, getrandbits
import math 
import time


class G:
	def __init__(self, p_length=1024):
		self.p, self.g = self.generate_prime_number(p_length)

	@staticmethod
	def generate_prime_candidate(length):
		# generate random bits
		p = getrandbits(length)
		# apply a mask to set MSB and LSB to 1
		p |= (1 << length - 1) | 1
		g1 = (p - 1)/2
		g2 = 2*p + 1

		return p, g1, g2

	def generate_prime_number(self, length):
		p, g1, g2 = 4, 4, 4
		iters = 0
		# keep generating while the primality test fail
		while True:
			iters += 1
			p, g1, g2 = self.generate_prime_candidate(length)
			if self.is_prime(p, 128) :
				print("Found p")

				if self.is_prime(g1, 128) :
					g = g1
					print(f'Found g in {iters} iterations it\'s (p - 1)/2 !')
					break
				elif self.is_prime(g2, 128) :
					g = g2
					print(f'Found g in {iters} iterations it\'s 2*p - 1 !')
					break

		return p, g

	# Miller-Rabin
	@staticmethod
	def is_prime(n, k=128):
		# Test if n is not even.
		# But care, 2 is prime !
		if n == 2 or n == 3:
			return True
		if n <= 1 or n % 2 == 0:
			return False
		# find r and s
		s = 0
		r = n - 1
		while r & 1 == 0:
			s += 1
			r //= 2
		# do k tests
		for _ in range(k):
			a = randrange(2, n - 1)
			x = pow(a, r, n)
			if x != 1 and x != n - 1:
				j = 1
				while j < s and x != n - 1:
					x = pow(x, 2, n)
					if x == 1:
						return False
					j += 1
				if x != n - 1:
					return False	
		return True

	@staticmethod
	def is_primitive_root(p, root):
		pass


G = G(256)
print(f'p = {G.p}')
print(f'g = {G.g}')

tic = time.time()
A = pow(G.g, getrandbits(1024), G.p)
print(f'{A}')
toc = time.time()
print(toc - tic)