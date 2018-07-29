class Solution(object):
	def stoneGame(self, piles):
		th = sum(piles)/2

		def win(ls, count):
			if count > th:
				return True
			if not ls:
				return False

			return (win(ls[2:], count + ls[0]) and win(ls[1:-1], count + ls[0])) or \
			       (win(ls[1:-1], count + ls[-1]) and win(ls[0:-2], count + ls[-1]))

		return win(piles, 0)



print Solution().stoneGame([1,2])