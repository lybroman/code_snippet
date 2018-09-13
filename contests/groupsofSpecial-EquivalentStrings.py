class Solution(object):
	def numSpecialEquivGroups(self, A):
		groups = []
		features = []
		for chs in A:
			odd = sorted(chs[1::2])
			even = sorted(chs[0::2])

			for i, (o, e) in enumerate(features):
				if o == odd and e == even:
					groups[i].append(chs)
					break
			else:
				groups.append([chs])
				features.append((odd, even))

		return len(groups)


A = ["a","b","c","a","c","c"]
print Solution().numSpecialEquivGroups(A)