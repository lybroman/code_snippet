class Solution(object):
	def primePalindrome(self, N):

		def is_prime(n):
			for i in xrange(2, int(n ** .5) + 1):
				if n % i == 0:
					return False

			return True

		def is_palindrome(n):
			n_reverse = 0
			m = n
			while n > 0:
				n_reverse = n_reverse * 10 + n % 10
				n /= 10

			if n_reverse == m:
				return True
			else:
				return False

		if N <=2: return 2

		while N % 2 == 0:
			N += 1

		while not is_palindrome(N) or not is_prime(N):
			N += 1

			if pow(10, 1) < N < pow(10, 2) and N!= 11: N = pow(10, 2)

			if pow(10, 3) < N < pow(10, 4): N = pow(10, 4)

			if pow(10, 5) < N < pow(10, 6): N = pow(10, 6)

			if pow(10, 7) < N < pow(10, 8): N = pow(10, 8)

		return N


class Solution1(object):
	def primePalindrome(self, N):
		def is_prime(n):
			return n > 1 and all(n % d for d in xrange(2, int(n**.5) + 1))

		def reverse(x):
			ans = 0
			while x:
				ans = 10 * ans + x % 10
				x /= 10
			return ans

		while True:
			if N == reverse(N) and is_prime(N):
				return N
			N += 1
			if 10**7 < N < 10**8:
				N = 10**8
import time

t = time.time()
print Solution1().primePalindrome(9939234)
print time.time() - t

t = time.time()
print Solution().primePalindrome(9939234)
print time.time() - t