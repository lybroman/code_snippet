class Solution(object):
	def numRescueBoats(self, people, limit):
		people.sort()

		def find_next(p, target):
			i, j = 0, len(p) - 1
			while i < j:
				mid = (i + j)/2
				if p[mid] == target:
					return mid
				elif p[mid] > target:
					j = mid - 1
				else:
					i = mid + 1

			if p[i] > target:
				return i - 1
			else:
				return i

		count = 0

		while people:

			if len(people) >= 2:
				n = find_next(people[1:], limit-people[0])
				count += 1
				if n >= 0:
					people.pop(0)
					people.pop(n)
				else:
					people.pop(0)
			else:
				count += 1
				people.pop(0)

			#print people

		return count


print Solution().numRescueBoats([3,5,3,4], 5)
print Solution().numRescueBoats([3,2,2,1], 3)
print Solution().numRescueBoats([1,2], 3)
print Solution().numRescueBoats([3,3], 3)
print Solution().numRescueBoats([5,1,4,2], 6)
print Solution().numRescueBoats([21,40,16,24,30], 50)



