from collections import defaultdict


class Solution(object):
	def buddyStrings(self, A, B):
		la, lb = len(A), len(B)
		if la != lb or not la or not lb:
			return False
		count = defaultdict(int)
		i = 0
		while i < la:
			if A[i] == B[i]:
				count[A[i]] += 1
				i += 1
			else:
				break

		if i == la:
			for key, value in count.items():
				if value >= 2:
					return True
			return False

		s0a = A[i]
		s0b = B[i]

		i += 1
		while i < la:
			if A[i] == B[i]:
				i += 1
			elif s0a == B[i] and s0b == A[i]:
				i += 1
				s0a = s0b = None
			else:
				return False

		return True


print Solution().buddyStrings("aaaaabc", "aaaaacb")
print Solution().buddyStrings("aa", "")
print Solution().buddyStrings("aa", "aa")
print Solution().buddyStrings("", "")
print Solution().buddyStrings("", "aa")
print Solution().buddyStrings("ab", "ab")
print Solution().buddyStrings("daaaabc", "aaaaacd")
print Solution().buddyStrings("daaaaaa", "aaaaaad")