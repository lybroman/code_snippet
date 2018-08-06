class Solution(object):
	def decodeAtIndex(self, S, K):
		size = 0
		for s in S:
			if s.isdigit():
				size *= int(s)
			else:
				size += 1

		for i in xrange(len(S) - 1, -1, -1):
			K %= size

			if S[i].isdigit():
				size /= int(S[i])
			elif K == 0:
				return S[i]
			else:
				size -= 1


S = "ha2s2"

print Solution().decodeAtIndex(S, 9)