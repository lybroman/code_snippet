from collections import defaultdict
class Solution(object):
	def isNStraightHand(self, hand, W):
		if len(hand) % W !=0:
			return False
		x = defaultdict(int)

		for h in hand:
			x[h] += 1

		unique_nums = sorted(x.keys())

		while unique_nums:
			i = unique_nums[0]

			for ii in xrange(W):
				if x[i + ii] > 0:
					x[i + ii] -= 1
				else:
					return False
				if x[i + ii] == 0:
					unique_nums.remove(i + ii)

		return True




hand = [1,2,3,4]
W = 2
print Solution().isNStraightHand(hand, W)