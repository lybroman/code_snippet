class Solution(object):
	def minEatingSpeed(self, piles, H):
		b = sum(piles)/H if sum(piles)/H > 0 else 1
		e = max(piles)

		while b <= e:

			k = (b + e) / 2
			b_finished = False

			if sum((p - 1) / k + 1 for p in piles) <= H:
				b_finished = True

			if b_finished:
				e = k - 1
			else:
				b = k + 1

		return b


piles = [3, 6, 7, 11]
H = 8
print Solution().minEatingSpeed(piles, H)


piles = [30,11,23,4,20]
H = 5
print Solution().minEatingSpeed(piles, H)

piles = [30,11,23,4,20]
H = 6
print Solution().minEatingSpeed(piles, H)

piles = [332484035]
H = 823855818

print Solution().minEatingSpeed(piles, H)
