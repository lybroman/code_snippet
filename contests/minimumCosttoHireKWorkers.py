import heapq
import fractions

class Solution(object):
	def mincostToHireWorkers(self, quality, wage, K):
		ratios = sorted([(fractions.Fraction(w, q), q) for w, q in zip(wage, quality)])
		h = []
		sumq = 0
		min_wag = float('inf')

		for r, q in ratios:
			heapq.heappush(h, -q)
			sumq += q

			if len(h) > K:
				sumq += heapq.heappop(h)

			if len(h) == K:
				min_wag = min(min_wag, sumq * r)

		return float(min_wag)



quality = [10,20,5]
wage = [70,50,30]
K = 2

print Solution().mincostToHireWorkers(quality, wage, K)


