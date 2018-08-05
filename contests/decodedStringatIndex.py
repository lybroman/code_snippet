class Solution(object):
	def decodeAtIndex(self, S, K):

		tape = []
		digit = [str(i) for i in xrange(1, 10)]

		for i in S:
			if i not in digit:
				tape.append()
			else:


			if len(tape) >= K:
				return tape[K - 1]


S = "ha22"
K = 5

print Solution.decodeAtIndex(S,K)