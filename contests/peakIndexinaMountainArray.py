class Solution(object):
	def peakIndexInMountainArray1(self, A):
		for i in xrange(1, len(A) - 1):
			if A[i + 1] < A[i] > A[i - 1]:
				return i

	def peakIndexInMountainArray(self, A):
		s, e = 0, len(A) - 1

		while s <= e:
			mid = (s + e)/2
			if 0 < mid < len(A) -1 and A[mid - 1] < A[mid] > A[mid + 1]:
				return mid

			elif A[mid - 1] < A[mid] < A[mid + 1]:
				s = mid + 1

			else:
				e = mid - 1


print Solution().peakIndexInMountainArray1([0, 2, 2, 3, 1, 1, 0])
print Solution().peakIndexInMountainArray([0, 2, 2, 3, 1, 1, 0])