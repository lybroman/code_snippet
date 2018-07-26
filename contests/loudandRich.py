from collections import defaultdict


class Solution(object):
	def loudAndRich(self, richer, quiet):
		comparison = defaultdict(list)
		for i in xrange(len(richer)):
			comparison[richer[i][1]].append(richer[i][0])

		ans = [None] * len(quiet)

		def dfs(i):
			if not ans[i]:
				ans[i] = i
				for j in comparison[i]:
					cand = dfs(j)
					if quiet[ans[i]] > quiet[cand]:
						ans[i] = cand

			return ans[i]

		return map(dfs, [_ for _ in xrange(len(quiet))])


#  [5,5,2,5,4,5,6,7]
richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]
print Solution().loudAndRich(richer, quiet)