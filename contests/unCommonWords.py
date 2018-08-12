from collections import  defaultdict
class Solution(object):
	def uncommonFromSentences(self, A, B):
		voc = defaultdict(int)
		A = A.strip().split(' ')
		B = B.strip().split(' ')
		for word in A:
			voc[word] += 1

		for word in B:
			voc[word] += 1

		ans = []
		for word in voc:
			if voc[word] <= 1:
				ans.append(word)

		return ans

A = "this apple is sweet"
B = "this apple is sour"
print Solution().uncommonFromSentences(A, B)

A = "apple apple"
B = "banana"
print Solution().uncommonFromSentences(A, B)
