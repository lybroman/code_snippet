class Solution(object):
	def numRescueBoats(self, people, limit):
		people.sort()
		num = 0
		while people:
			if len(people) == 1:
				return num + 1
			if people[-1] + people[0] <= limit:
				people.pop(0)

			num += 1
			people.pop(-1)

		return num

print Solution().numRescueBoats([3,5,3,4], 5)
print Solution().numRescueBoats([3,2,2,1], 3)
print Solution().numRescueBoats([1,2], 3)
print Solution().numRescueBoats([3,3], 3)
print Solution().numRescueBoats([5,1,4,2], 6)
print Solution().numRescueBoats([21,40,16,24,30], 50)



