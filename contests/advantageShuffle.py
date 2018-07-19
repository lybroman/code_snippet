class Solution(object):
	def advantageCount(self, A, B):
		class IndexItem():
			def __init__(self, value, index):
				self.value = value
				self.index= index

		l = len(A)
		As = []
		Bs = []
		for i in range(l):
			As.append(IndexItem(A[i], i))
			Bs.append(IndexItem(B[i], i))

		As.sort(cmp=lambda x, y: 1 if x.value >= y.value else -1, reverse=True)
		Bs.sort(cmp=lambda x, y: 1 if x.value >= y.value else -1, reverse=True)

		Amax = []
		Bmin = []
		res = ['a' for _ in range(l)]
		i = 0
		j = 0
		while i < l and j < l:
			if As[i].value > Bs[j].value:
				Amax.append(As[i])
				Bmin.append(Bs[j])
				res[Bmin[i].index] = Amax[i].value
				As[i].index = -1;
				i += 1
				j += 1
			else:
				j += 1

		j = 0
		for i in range(l):
			if As[i].index != -1:
				while res[j] != 'a':
					j += 1
				res[j] = As[i].value

		return res

A = [2,7,11,15]
B = [1,10,4,11]

print Solution().advantageCount(A, B)