class Solution(object):
	def lemonadeChange(self, bills):
		money = {5:0, 10:0, 20:0}

		for pay in bills:
			if pay == 5:
				money[5] += 1

			if pay == 10:
				if money[5] > 0:
					money[5] -= 1
					money[10] += 1
				else:
					return False

			if pay == 20:
				if money[10] > 0:
					money[10] -= 1
					if money[5] > 0:
						money[5] -= 1
						money[20] += 1
					else:
						return False
				elif money[5] > 2:
					money[5] -= 3
					money[20] += 1
				else:
					return False
		return True


print Solution().lemonadeChange([5,5,5,20,5,5,5,20,5,5,5,10,5,20,10,20,10,20,5,5])



